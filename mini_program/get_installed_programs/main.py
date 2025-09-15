import winreg
import os

def get_installed_programs():
    programs = []
    # Registry paths where information about installed programs is stored
    registry_paths = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    ]

    for path in registry_paths:
        try:
            # Open the registry key
            registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path, 0, winreg.KEY_READ)
            i = 0
            while True:
                try:
                    # Enumerate all subkeys
                    subkey_name = winreg.EnumKey(registry_key, i)
                    subkey = winreg.OpenKey(registry_key, subkey_name)
                    
                    # Get the program name if it exists
                    try:
                        display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                        programs.append(display_name)
                    except FileNotFoundError:
                        pass
                    
                    winreg.CloseKey(subkey)
                    i += 1
                except OSError:
                    break
            winreg.CloseKey(registry_key)
        except OSError:
            pass
    return sorted(list(set(programs))) # Remove duplicates and sort

if __name__ == "__main__":
    program_list = get_installed_programs()
    
    # Save the list to a file
    with open("installed_programs.txt", "w", encoding="utf-8") as f:
        for program in program_list:
            f.write(program + "\n")
            
    print("The list of installed programs has been saved to installed_programs.txt")
