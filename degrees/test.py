import os
import subprocess
import sys

# Define the path to the problematic executable
executable_path = 'C:\\Python312\\Scripts\\check50.exe'

# Check if the executable exists and try to remove it
if os.path.exists(executable_path):
    try:
        os.remove(executable_path)
        print(f"Removed existing file at: {executable_path}")
    except OSError as e:
        print(f"Error removing file: {e.strerror}. Please check your permissions.")

# Attempt to reinstall the packages using pip
# Ensure pip is updated and use subprocess to call pip install for the required packages
try:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'jinja2', 'cffi', 'certifi', 'beautifulsoup4', 'attrs', 'requests', 'cryptography', 'lib50', 'check50'])
    print("Packages installed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Package installation failed: {e}")
