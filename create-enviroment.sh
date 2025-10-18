#!/bin/sh

# Define the name of the virtual environment directory
VENV_DIR=".venv"

# Check if the virtual environment directory exists

if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment '$VENV_DIR' not found."
    echo "Creating virtual environment..."
    
    # Command to create the virtual environment
    python3 -m venv "$VENV_DIR"
    
    # Check if the creation was successful
    if [ $? -eq 0 ]; then
        echo "Virtual environment created successfully. To activate, run: source $VENV_DIR/bin/activate"
    else
        echo "ERROR: Failed to create virtual environment. Ensure python3 is installed."
    fi
else
    echo "Virtual environment '$VENV_DIR' already exists. Skipping creation."
    echo "To activate, run: source $VENV_DIR/bin/activate"
fi
