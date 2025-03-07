import os
import shutil

def selective_copy(source_folder, destination_folder, file_extension):
    """Copies all files of a given type from source_folder and subfolders to destination_folder."""
    
    # Ensure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)

    # Walk through directory tree
    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.lower().endswith(file_extension.lower()):
                source_path = os.path.join(foldername, filename)
                destination_path = os.path.join(destination_folder, filename)

                # Copy the file to the new location
                shutil.copy2(source_path, destination_path)
                print(f"✅ Copied: {source_path} → {destination_path}")

    print("\n🎉 Selective Copy Complete!")

if __name__ == "__main__":
    # Ask user for details
    source = input("Enter the source folder path: ").strip()
    destination = input("Enter the destination folder path: ").strip()
    extension = input("Enter the file extension to copy (e.g., .txt, .jpg): ").strip()

    if not os.path.exists(source):
        print("❌ ERROR: The source folder does not exist.")
    else:
        selective_copy(source, destination, extension)
