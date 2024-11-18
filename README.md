# RMBPrompt Extractor

## Overview

This Python script, `rmbprompt.py`, is designed to extract a prompt from a PNG image's metadata and copy it to the clipboard. It can be particularly useful when working with generative art or images where the creation parameters are embedded within the image.

The script is intended to be used via the right mouse button menu in Windows Explorer, allowing you to extract and copy prompts directly from the context menu of PNG files.

## Requirements

- Python 3.x
- `Pillow` library (for handling image files)
- `pyperclip` library (for copying text to the clipboard)

### Recommended: Use a Virtual Environment

To avoid conflicts with other Python projects, it is highly recommended to use a virtual environment. Here’s how you can set one up:

1. **Create a Virtual Environment**:
   ```sh
   python -m venv venv
   ```

2. **Activate the Virtual Environment**:
   - On Windows:
     ```sh
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source venv/bin/activate
     ```

3. **Install Required Libraries**:
   ```sh
   pip install Pillow pyperclip
   ```

## Usage

### Command Line

To use the script from the command line, you need to provide the path to a PNG file as an argument. The script will then extract the prompt from the image's metadata and copy it to your clipboard.

```sh
python rmbprompt.py <path_to_png>
```

### Example

Assuming you have a PNG file named `example.png` in the current directory:

```sh
python rmbprompt.py example.png
```

If the script finds and extracts a valid prompt, it will print the prompt to the console and copy it to your clipboard.

### Right Mouse Button Menu in Windows Explorer

To integrate this script into the right mouse button menu for PNG files in Windows Explorer, use the provided `template.reg` file. This file registers the script as a shell extension for PNG files.

1. **Edit `template.reg`**:
   - Open `template.reg` in a text editor.
   - Replace `C:\\Path\\To\\Python.exe` with the actual path to your Python executable (e.g., `C:\\Users\\YourUsername\\path\\to\\venv\\Scripts\\python.exe` if using a virtual environment).
   - Replace `C:\\Path\\To\\rmbprompt.py` with the actual path to the `rmbprompt.py` script.

2. **Apply the Registry Changes**:
   - Double-click `template.reg` and confirm the prompt to add the information to the Windows registry.
   - After applying the changes, right-click on any PNG file in Windows Explorer to see the "Copy Prompt to Clipboard" option.

#### Contents of `template.reg`

```reg
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\SystemFileAssociations\.png\shell\ExtractPrompt]
@="Copy Prompt to Clipboard"

[HKEY_CLASSES_ROOT\SystemFileAssociations\.png\shell\ExtractPrompt\command]
@="\"C:\\Path\\To\\Python.exe\" \"C:\\Path\\To\\rmbprompt.py\" \"%1\""
```

## How It Works

1. **Open the Image**: The script uses the `Pillow` library to open the PNG file.
2. **Access Metadata**: It checks the image's metadata for a key named `"prompt"` (or another specified key).
3. **Parse JSON**: If the metadata is found, it attempts to parse the JSON content.
4. **Extract Prompt**: The script looks for a specific structure in the JSON where a field with "String Literal" in its title contains an input string. This string is considered the prompt.
5. **Copy to Clipboard**: If a valid prompt is found, it is copied to the clipboard using the `pyperclip` library.

## Error Handling

- If no metadata is found or if the metadata structure does not match the expected format, the script will print an appropriate message.
- Any exceptions encountered during execution are caught and printed to help with debugging.

## Notes

- Ensure that the PNG file you are working with has the necessary metadata embedded. The key used in the script (`"prompt"`) may need to be adjusted based on the actual metadata structure of your images.
- The script assumes a specific JSON structure for the metadata. If this structure varies, you may need to modify the script accordingly.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to modify and enhance this script to better suit your needs!
