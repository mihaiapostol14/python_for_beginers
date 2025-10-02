import os
import shutil 

# --- Settings ---
# IMPORTANT: Set the correct path to the folder where all your projects are stored!
ROOT_DIR = os.getcwd()
VENV_NAME = "venv"
# --- End of settings ---

def find_and_remove_venvs(root_path, venv_name):
    for dirpath, dirnames, filenames in os.walk(root_path):
        if venv_name in dirnames:
            venv_path = os.path.join(dirpath, venv_name)
            print(f"Found virtual environment: {venv_path}")
            try:
                shutil.rmtree(venv_path)
                print(f"✅ Removed: {venv_path}")
            except Exception as e:
                print(f"❌ Error while removing {venv_path}: {e}")

# Run function
if __name__ == "__main__":
    if not os.path.isdir(ROOT_DIR):
        print(f"Error: Specified path not found: {ROOT_DIR}")
    else:
        find_and_remove_venvs(root_path=ROOT_DIR, venv_name=VENV_NAME)
