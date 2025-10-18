#!/bin/sh
TOOL_NAME="pip-compile"
# The 'if ! command -v' structure implements the "if not" logic.
# 'command -v $TOOL_NAME' returns success (0) if found, and failure (non-zero) if NOT found.
# The '!' negates the result, so the 'then' block runs only if the command was NOT found.
if ! command -v "$TOOL_NAME" &> /dev/null
then
    echo "⚠️ Warning: $TOOL_NAME was not found."
    echo "Executing 'pip install pip-tools'..."
    
    # Execute the installation command
    pip install pip-tools
    
    # Check the exit code of the installation command
    if [ $? -eq 0 ]; then
        echo "🎉 Installation completed successfully!"
    else
        echo "❌ Error: The installation of pip-tools failed."
    fi
else
    echo "✅ Success: $TOOL_NAME is already installed. No action needed!"
fi

pip-compile requirements.in
pip install -r requirements.txt