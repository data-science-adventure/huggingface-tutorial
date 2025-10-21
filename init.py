import subprocess
import sys
import os

# --- Virtual Environment Configuration ---
# Define the name of the virtual environment directory.
VENV_DIR = ".venv"

def obtener_python_venv():
    """Returns the path to the Python executable inside the .venv."""
    # Handles path differences between Windows and Unix/Linux/macOS
    if sys.platform == "win32":
        return os.path.join(VENV_DIR, "Scripts", "python.exe")
    else:
        return os.path.join(VENV_DIR, "bin", "python")

def obtener_pip_venv():
    """Returns the base command for running pip inside the .venv."""
    # Using 'python -m pip' is the most reliable way to run pip in any environment.
    return [obtener_python_venv(), '-m', 'pip']
    
# --- Utility Functions ---

def ejecutar_comando(comando, success_message, error_message):
    """Executes a system command and handles errors."""
    command_str = ' '.join(comando)
    print(f"\n🚀 Executing: {command_str}")
    try:
        # check=True raises CalledProcessError if the command fails
        subprocess.run(comando, check=True, text=True, capture_output=True, timeout=120) 
        print(f"✅ Success! {success_message}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error! {error_message}")
        # Show error output if available
        if e.stderr:
             print(f"Error details (stderr): \n{e.stderr.strip()}")
        return False
    except FileNotFoundError:
        print(f"❌ Error! The main command was not found. Ensure it's installed and in your PATH.")
        print(f"Attempted command: {command_str}")
        return False
    except subprocess.TimeoutExpired:
        print(f"❌ Error! Command '{command_str}' timed out and was cancelled.")
        return False
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return False

# --- Menu Options ---

def create_virtual_environment():
    """Creates a Python virtual environment named '.venv'."""
    if os.path.isdir(VENV_DIR):
        print(f"⚠️ Directory '{VENV_DIR}' already exists. Skipping creation.")
        # Ensure the venv directory is usable
        if os.path.exists(obtener_python_venv()):
            print("✅ Existing .venv seems valid.")
            return True
        else:
            print("❌ Existing .venv seems invalid (python executable missing). Please delete and try again.")
            return False
        
    command = [sys.executable, '-m', 'venv', VENV_DIR]
    success_msg = f"Virtual environment '{VENV_DIR}' created successfully."
    error_msg = f"Could not create the virtual environment '{VENV_DIR}'."
    
    if ejecutar_comando(command, success_msg, error_msg):
        # Once created, ensure pip and setuptools are updated inside the new venv
        print("\n🛠️ Updating pip and setuptools inside .venv...")
        update_command = obtener_pip_venv() + ['install', '--upgrade', 'pip', 'setuptools']
        ejecutar_comando(update_command, "Pip and setuptools updated.", "Could not update pip/setuptools.")
        return True
    return False

def verify_and_install_pip_compile():
    """Installs 'pip-tools' (which provides pip-compile) INSIDE the .venv."""
    if not os.path.isdir(VENV_DIR):
        print(f"🛑 Error: Virtual environment '{VENV_DIR}' does not exist. Please create it (Option 1) before installing requirements.")
        return False
        
    print("\n--- Ensuring 'pip-tools' is installed in .venv ---")
    
    # We install 'pip-tools' into the .venv using its 'pip'.
    # This acts as both a check and an install step, as pip is smart enough 
    # to skip the install if the package is already present.
    
    # Command: [venv_python, -m, pip, install, pip-tools]
    install_command = obtener_pip_venv() + ['install', 'pip-tools']
    success_msg = "'pip-tools' (which includes pip-compile) has been installed INSIDE .venv."
    error_msg = "Could not install 'pip-tools' inside .venv."
    
    print("⏳ Attempting to install pip-tools directly into .venv...")
    
    if ejecutar_comando(install_command, success_msg, error_msg):
        return True
    else:
        print("\n🛑 Could not ensure 'pip-tools' installation in .venv. Stopping requirements installation.")
        return False

def install_requirements():
    """
    Installs dependencies INSIDE the .venv:
    1. Ensures .venv exists.
    2. Installs pip-compile inside .venv.
    3. Compiles requirements.in to requirements.txt.
    4. Installs packages from requirements.txt.
    """
    if not os.path.isdir(VENV_DIR):
        print(f"\n🛑 Error: The virtual environment '{VENV_DIR}' does not exist. Please create the environment (Option 1) before installing requirements.")
        return
    
    # 1. Verify and install pip-tools INSIDE the .venv
    if not verify_and_install_pip_compile():
        return # Stop if installation fails

    # The next commands must explicitly use executables/modules from within the .venv.
    
    python_venv = obtener_python_venv()
    
    # 2. Command to compile: [pip-compile executable from venv, requirements.in]
    # We construct the path to the pip-compile executable within the venv
    pip_compile_venv = os.path.join(os.path.dirname(python_venv), "pip-compile")
    if sys.platform == "win32":
         pip_compile_venv += ".exe"
    
    # Using the direct path to the executable is the most explicit way.
    if not os.path.exists(pip_compile_venv):
        print("🔴 Warning: Could not find 'pip-compile' executable. Falling back to 'python -m piptools compile'.")
        compile_command = [python_venv, '-m', 'piptools', 'compile', 'requirements.in']
    else:
        compile_command = [pip_compile_venv, 'requirements.in']

    success_msg_compile = "requirements.txt compiled/updated successfully INSIDE .venv."
    error_msg_compile = "Could not compile 'requirements.in'. Ensure 'requirements.in' exists."

    # 3. Command to install: [venv_python, -m, pip, install, -r, requirements.txt]
    install_command = obtener_pip_venv() + ['install', '-r', 'requirements.txt']
    success_msg_install = "All dependencies installed successfully INSIDE .venv."
    error_msg_install = "Could not install packages from 'requirements.txt'."

    # Execute sequentially
    
    # A. Compile
    print("\n--- Step 1: Compiling requirements.in ---")
    if not ejecutar_comando(compile_command, success_msg_compile, error_msg_compile):
        return # Stop if compilation fails

    # B. Install
    print("\n--- Step 2: Installing from requirements.txt ---")
    if os.path.exists("requirements.txt"):
        ejecutar_comando(install_command, success_msg_install, error_msg_install)
    else:
        print("🔴 Cannot install. The 'requirements.txt' file was not generated or does not exist after compilation.")


# --- Main Function ---

def show_menu():
    """Displays the main menu and handles user interaction."""
    while True:
        print("\n" + "="*50)
        print("🤖 Python Project Setup Assistant")
        print("="*50)
        print("1. 📁 Create and prepare the virtual environment (.venv)")
        print("2. 📦 Install requirements (in .venv)")
        print("3. 🚪 Exit")
        print("-" * 50)

        option = input("Choose an option (1-3): ").strip()

        if option == '1':
            create_virtual_environment()
        elif option == '2':
            install_requirements()
        elif option == '3':
            print("\n👋 Thanks for using the Setup Assistant! Happy coding!")
            sys.exit(0)
        else:
            print("\n🚨 Invalid option. Please select 1, 2, or 3.")

# Script entry point
if __name__ == "__main__":
    show_menu()