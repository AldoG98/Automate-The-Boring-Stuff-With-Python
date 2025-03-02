import re
import os

def mad_libs(file_path):
    """Reads a Mad Libs template file and replaces placeholders with user input."""
    
    # Ensure the file exists
    if not os.path.exists(file_path):
        print(f"❌ ERROR: The file '{file_path}' was not found.")
        return
    
    # Read the template
    with open(file_path, "r") as file:
        story = file.read()

    # Define placeholders (expandable list)
    placeholders = re.findall(r"\b(ADJECTIVE|NOUN|VERB|ADVERB|PLACE|PERSON)\b", story)

    # Replace each placeholder with user input
    for word in placeholders:
        user_input = input(f"Enter a {word.lower()}: ").strip()
        story = story.replace(word, user_input, 1)  # Replace one occurrence at a time

    # Display the final story
    print("\n✅ Your Mad Libs Story:\n")
    print(story)

if __name__ == "__main__":
    # Path to the Mad Libs template file (modifiable)
    file_path = "madlibs_template.txt"
    mad_libs(file_path)
