import os
import subprocess

# --- Settings ---
ROOT_DIR = os.getcwd()
VENV_NAME = "venv"
# --- End of settings ---

def setup_project_envs(root_path, venv_name):
    for dirpath, dirnames, filenames in os.walk(root_path):
        # Only check first-level project dirs
        if dirpath == root_path:
            for project in dirnames:
                project_path = os.path.join(root_path, project)
                venv_path = os.path.join(project_path, venv_name)
                req_file = os.path.join(project_path, "requirements.txt")

                # 1. Create venv if missing
                if not os.path.isdir(venv_path):
                    print(f"Creating venv in: {project_path}")
                    try:
                        subprocess.check_call(["python", "-m", "venv", venv_path])
                        print(f"✅ Created: {venv_path}")
                    except Exception as e:
                        print(f"❌ Error creating venv in {project_path}: {e}")
                        continue
                else:
                    print(f"Skipped (venv exists): {venv_path}")

                # 2. Install requirements if file exists
                if os.path.isfile(req_file):
                    print(f"Installing requirements for: {project}")
                    pip_exe = os.path.join(venv_path, "Scripts", "pip.exe")  # Windows
                    try:
                        subprocess.check_call([pip_exe, "install", "-r", req_file])
                        print(f"✅ Installed requirements in {project}")
                    except Exception as e:
                        print(f"❌ Error installing requirements in {project}: {e}")
                else:
                    print(f"No requirements.txt found in {project}")

            break  # stop after first level

# Run
if __name__ == "__main__":
    if not os.path.isdir(ROOT_DIR):
        print(f"Error: Specified path not found: {ROOT_DIR}")
    else:
        setup_project_envs(root_path=ROOT_DIR, venv_name=VENV_NAME)
