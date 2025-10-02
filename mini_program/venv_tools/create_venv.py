import os
import subprocess

# --- Settings ---
ROOT_DIR = os.getcwd()
VENV_NAME = "venv"
# --- End of settings ---

def find_and_create_venvs(root_path, venv_name):
    for dirpath, dirnames, filenames in os.walk(root_path):
        # Only check top-level project directories, skip nested dirs
        if dirpath == root_path:
            for project in dirnames:
                project_path = os.path.join(root_path, project)
                venv_path = os.path.join(project_path, venv_name)

                if not os.path.isdir(venv_path):
                    print(f"Creating venv in: {project_path}")
                    try:
                        subprocess.check_call(["python", "-m", "venv", venv_path])
                        print(f"✅ Created: {venv_path}")
                    except Exception as e:
                        print(f"❌ Error while creating venv in {project_path}: {e}")
                else:
                    print(f"Skipped (already exists): {venv_path}")
            break  # stop after scanning top-level dirs

# Run function
if __name__ == "__main__":
    if not os.path.isdir(ROOT_DIR):
        print(f"Error: Specified path not found: {ROOT_DIR}")
    else:
        find_and_create_venvs(root_path=ROOT_DIR, venv_name=VENV_NAME)
