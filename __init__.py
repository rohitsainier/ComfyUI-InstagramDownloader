from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
import os
import subprocess
import sys

# Install dependencies


def install_deps():
    try:
        requirements_path = os.path.join(
            os.path.dirname(__file__), "requirements.txt")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", requirements_path])
        print("Successfully installed dependencies!")
    except Exception as e:
        print(f"Error installing dependencies: {e}")


# Try to install dependencies on first import
try:
    import instaloader
except ImportError:
    print("Installing required dependencies...")
    install_deps()


__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
