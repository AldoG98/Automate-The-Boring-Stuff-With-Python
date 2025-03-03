import os
import re

def search_regex_in_files(directory, pattern):
    """Searches for a regex pattern in all .txt files within a directory."""
    try:
        regex = re.compile(pattern)  # Compile user regex
    except re.error:
        print("❌ Invalid regex pattern. Please try again.")
        return

    print("\n🔍 Searching for matches...\n")

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)

            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()

            # Search for matches line by line
            matches_found = False
            for line_num, line in enumerate(lines, start=1):
                if regex.search(line):
                    if not matches_found:
                        print(f"\n📄 Matches in '{filename}':")
                        matches_found = True
                    print(f"  Line {line_num}: {line.strip()}")

    print("\n✅ Search complete.")

if __name__ == "__main__":
    # Set the directory where .txt files are stored
    directory = r"C:\Users\aldog\OneDrive\Desktop\pythonvscode\Automate the boring stuff with python\Project 11"

    # Ensure directory exists
    if not os.path.exists(directory):
        print(f"❌ ERROR: Directory '{directory}' not found.")
    else:
        # Get user input for regex pattern
        user_pattern = input("Enter a regex pattern to search for: ").strip()
        search_regex_in_files(directory, user_pattern)
