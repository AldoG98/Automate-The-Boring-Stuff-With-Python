def comma_code(items):
    """Converts a list into a comma-separated string with 'and' before the last item."""
    if not items:  # Handle empty list
        return "The list is empty."
    elif len(items) == 1:  # Handle single-item list
        return items[0]
    else:
        return ", ".join(items[:-1]) + f", and {items[-1]}"

def get_user_list():
    """Prompts the user to enter items for a list."""
    items = []
    print("Enter items one by one. Type 'done' when finished:")
    
    while True:
        item = input("> ").strip()
        if item.lower() == 'done':
            break
        elif item:  # Prevent empty inputs from being added
            items.append(item)
        else:
            print("Please enter a valid item.")
    
    return items

while True:
    user_list = get_user_list()
    print("\nFormatted list:")
    print(comma_code(user_list))

    # Ask the user if they want to enter another list
    run_again = input("\nWould you like to enter another list? (y/n): ").strip().lower()
    if run_again != 'y':
        print("Goodbye!")
        break
