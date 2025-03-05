import sys
import json
import pyperclip
import os

# File to store clipboard data
CLIPBOARD_FILE = "clipboard.json"

def load_clipboard():
    """Loads clipboard data from the JSON file."""
    if os.path.exists(CLIPBOARD_FILE):
        with open(CLIPBOARD_FILE, "r") as file:
            return json.load(file)
    return {}

def save_clipboard(data):
    """Saves clipboard data to the JSON file."""
    with open(CLIPBOARD_FILE, "w") as file:
        json.dump(data, file, indent=4)

def main():
    clipboard = load_clipboard()

    if len(sys.argv) < 2:
        print("Usage: python multiclipboard.py [save|load|delete|list|update|search|clear] [key] [optional value]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "save":
        if len(sys.argv) < 3:
            print("❌ Error: Please provide a key to save the clipboard content.")
            sys.exit(1)
        key = sys.argv[2]
        clipboard[key] = pyperclip.paste()
        save_clipboard(clipboard)
        print(f"✅ Saved clipboard content under key: '{key}'")

    elif command == "load":
        if len(sys.argv) < 3:
            print("❌ Error: Please provide a key to load clipboard content.")
            sys.exit(1)
        key = sys.argv[2]
        if key in clipboard:
            pyperclip.copy(clipboard[key])
            print(f"✅ Copied '{key}' to clipboard.")
        else:
            print(f"❌ Error: Key '{key}' not found.")

    elif command == "delete":
        if len(sys.argv) < 3:
            print("❌ Error: Please provide a key to delete.")
            sys.exit(1)
        key = sys.argv[2]
        if key in clipboard:
            del clipboard[key]
            save_clipboard(clipboard)
            print(f"✅ Deleted '{key}' from clipboard.")
        else:
            print(f"❌ Error: Key '{key}' not found.")

    elif command == "list":
        if clipboard:
            print("\n📋 Saved Clipboard Snippets:")
            for key in clipboard:
                print(f"  🔹 {key}: {clipboard[key]}")
        else:
            print("📂 No saved clipboard snippets.")

    elif command == "update":
        if len(sys.argv) < 3:
            print("❌ Error: Please provide a key to update.")
            sys.exit(1)
        key = sys.argv[2]
        if key in clipboard:
            clipboard[key] = pyperclip.paste()
            save_clipboard(clipboard)
            print(f"✅ Updated clipboard content for key: '{key}'")
        else:
            print(f"❌ Error: Key '{key}' not found.")

    elif command == "search":
        if len(sys.argv) < 3:
            print("❌ Error: Please provide a search keyword.")
            sys.exit(1)
        keyword = sys.argv[2].lower()
        results = {k: v for k, v in clipboard.items() if keyword in k.lower() or keyword in v.lower()}
        if results:
            print("\n🔍 Search Results:")
            for k, v in results.items():
                print(f"  🔹 {k}: {v}")
        else:
            print(f"❌ No results found for '{keyword}'.")

    elif command == "clear":
        confirmation = input("⚠️ Are you sure you want to clear all clipboard data? (y/n): ").strip().lower()
        if confirmation == 'y':
            clipboard.clear()
            save_clipboard(clipboard)
            print("✅ Clipboard storage cleared.")
        else:
            print("❌ Operation canceled.")

    else:
        print("❌ Invalid command. Use: save, load, delete, list, update, search, or clear.")

if __name__ == "__main__":
    main()
