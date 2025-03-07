import os

def find_large_files(folder, size_threshold):
    """Finds and optionally deletes files larger than a specified size."""
    size_threshold_bytes = size_threshold * 1024 * 1024  # Convert MB to bytes

    # Walk through directory tree
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            try:
                file_size = os.path.getsize(file_path)
                if file_size >= size_threshold_bytes:
                    print(f"\n📁 Large File Found: {file_path} ({file_size / (1024*1024):.2f} MB)")
                    
                    # Ask for user confirmation before deletion
                    confirm = input("❌ Delete this file? (y/n): ").strip().lower()
                    if confirm == 'y':
                        os.remove(file_path)
                        print("✅ File Deleted.")
                    else:
                        print("⏩ Skipping file.")
            except Exception as e:
                print(f"⚠️ Error accessing {file_path}: {e}")

if __name__ == "__main__":
    # Ask user for directory and size threshold
    target_folder = input("Enter the folder path to scan: ").strip()
    size_limit = int(input("Enter the file size threshold in MB (e.g., 100): ").strip())

    if not os.path.exists(target_folder):
        print("❌ ERROR: The specified folder does not exist.")
    else:
        find_large_files(target_folder, size_limit)
