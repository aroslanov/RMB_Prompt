import json
import sys
import pyperclip
from PIL import PngImagePlugin, Image

def extract_prompt(png_file_path):
    try:
        # Open PNG and access its metadata
        img = Image.open(png_file_path)
        metadata = img.info.get("prompt", None)  # Replace "prompt" with the correct key if different
        
        if not metadata:
            print("No prompt metadata found in the file.")
            return

        # Parse the metadata JSON
        metadata_json = json.loads(metadata)
        for key, value in metadata_json.items():
            if "String Literal" in value["_meta"]["title"]:
                # Extract the prompt from the "inputs" field
                prompt = value["inputs"].get("string", None)
                if prompt:
                    pyperclip.copy(prompt)
                    print(f"Prompt copied to clipboard: {prompt}")
                    return
        print("No valid prompt found in the metadata.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_prompt.py <path_to_png>")
    else:
        extract_prompt(sys.argv[1])
