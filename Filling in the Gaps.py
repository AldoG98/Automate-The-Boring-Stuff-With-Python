import os
import re
import shutil

def find_files_with_prefix(folder, prefix):
    """Finds all files with the given prefix and extracts their numbers."""
    file_pattern = re.compile(rf"^{re.escape(prefix)}(\d+)(\.\w+)$")  # Matches 'prefix001.txt', 'prefix002.txt', etc.
    
    files = []
    for filename in os.listdir(folder):
        match = file_pattern.match(filename)
        if match:
            files.append((int(match.group(1)), filename, match.group(2)))  # (number, filename, extension)

    files.sort()  # Sort files based on their sequence number
    return files

def fill_gaps(folder, prefix):
    """Renames files with a sequential numbering pattern to remove gaps."""
    files = find_files_with_prefix(folder, prefix)

    if not files:
        print("❌ No files found with the given prefix.")
        return

    expected_number = 1  # Start numbering from 1
    for number, filename, extension in files:
        correct_filename = f"{prefix}{expected_number:03d}{extension}"
        current_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, correct_filename)

        if filename != correct_filename:
            shutil.move(current_path, new_path)
            print(f"🔄 Renamed: {filename} → {correct_filename}")

        expected_number += 1

    print("\n✅ File renaming complete! All gaps are filled.")

if __name__ == "__main__":
    folder = input("Enter the folder path: ").strip()
    prefix = input("Enter the filename prefix (e.g., 'file_'): ").strip()

    if not os.path.exists(folder):
        print("❌ ERROR: The specified folder does not exist.")
    else:
        fill_gaps(folder, prefix)
