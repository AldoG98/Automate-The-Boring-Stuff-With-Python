import re

def regex_strip(text, char=None):
    """Mimics the behavior of str.strip() using regex."""
    if char is None:  # Default case: Remove whitespace
        return re.sub(r"^\s+|\s+$", "", text)
    else:  # Remove specified character from both ends
        pattern = f"^[{re.escape(char)}]+|[{re.escape(char)}]+$"
        return re.sub(pattern, "", text)

while True:
    user_text = input("\nEnter a string to strip: ").strip()
    remove_char = input("Enter a character to strip (leave blank to remove whitespace): ").strip()

    if remove_char == "":
        result = regex_strip(user_text)
    else:
        result = regex_strip(user_text, remove_char)

    print(f"✅ Stripped Result: '{result}'")

    # Ask if the user wants to strip another string
    retry = input("\nWould you like to strip another string? (y/n): ").strip().lower()
    if retry != 'y':
        print("Goodbye!")
        break
