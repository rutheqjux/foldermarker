# FolderMarker

FolderMarker is a Python program designed to customize folder icons and labels for better organization and quick identification on Windows. By using FolderMarker, you can change the appearance of your folders to make them more easily recognizable.

## Features

- Change folder icons to any `.ico` file.
- Set custom labels for folders to provide additional context or information.
  
## Requirements

- Windows Operating System
- Python 3.x

## Installation

1. Clone the repository or download the `folder_marker.py` file.
2. Ensure your Python environment is set up on your system.

## Usage

To use FolderMarker, open a command prompt and run:

```bash
python folder_marker.py <folder_path> <icon_path> <label>
```

- `<folder_path>`: The path to the folder you want to customize.
- `<icon_path>`: The path to the `.ico` file you want to set as the folder icon.
- `<label>`: The label you want to assign to the folder.

### Example

```bash
python folder_marker.py "C:\Users\User\Documents\MyFolder" "C:\Icons\MyIcon.ico" "My Important Folder"
```

This command will set the folder icon to `MyIcon.ico` and label it as "My Important Folder".

## Notes

- The program modifies the `desktop.ini` file inside the specified folder to apply changes. This file must not be deleted for the customization to persist.
- Some changes might require a refresh or restart of Windows Explorer to take effect.

## Disclaimer

This program is designed for educational purposes. Use it responsibly and ensure you have backups of important data before operating on system files.

## License

This project is licensed under the MIT License - see the LICENSE file for details.