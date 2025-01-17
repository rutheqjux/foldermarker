import os
import sys
import ctypes
import shutil

def change_folder_icon(folder_path, icon_path):
    desktop_ini_content = """
    [.ShellClassInfo]
    IconResource={},0
    """.format(icon_path)

    desktop_ini_path = os.path.join(folder_path, "desktop.ini")
    
    with open(desktop_ini_path, "w") as desktop_ini_file:
        desktop_ini_file.write(desktop_ini_content.strip())

    ctypes.windll.kernel32.SetFileAttributesW(desktop_ini_path, 0x02)  # Hidden attribute
    ctypes.windll.kernel32.SetFileAttributesW(folder_path, 0x02)       # System attribute

def change_folder_label(folder_path, label):
    desktop_ini_path = os.path.join(folder_path, "desktop.ini")
    
    if not os.path.exists(desktop_ini_path):
        print("The desktop.ini file does not exist. You need to set an icon first.")
        return
    
    with open(desktop_ini_path, "r") as desktop_ini_file:
        lines = desktop_ini_file.readlines()

    with open(desktop_ini_path, "w") as desktop_ini_file:
        for line in lines:
            if line.startswith("[.ShellClassInfo]"):
                desktop_ini_file.write(line)
                desktop_ini_file.write("InfoTip={}\n".format(label))
            else:
                desktop_ini_file.write(line)

def main():
    if len(sys.argv) != 4:
        print("Usage: python folder_marker.py <folder_path> <icon_path> <label>")
        sys.exit(1)

    folder_path = sys.argv[1]
    icon_path = sys.argv[2]
    label = sys.argv[3]

    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        sys.exit(1)

    if not os.path.exists(icon_path):
        print("The specified icon file does not exist.")
        sys.exit(1)

    change_folder_icon(folder_path, icon_path)
    change_folder_label(folder_path, label)
    print("Folder customization complete!")

if __name__ == "__main__":
    main()