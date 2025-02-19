def get_valid_integer(prompt):
    """Prompts the user for a valid positive integer and handles errors."""
    while True:
        try:
            user_input = int(input(prompt))
            if user_input > 0:
                return user_input
            else:
                print("Error: Please enter a positive integer greater than zero.")
        except ValueError:
            print("Error: Invalid input! Please enter a valid integer.")

while True:
    number = get_valid_integer("Enter a positive integer: ")
    print(f"You entered: {number}")

    # Ask the user if they want to try again
    run_again = input("\nWould you like to enter another number? (y/n): ").strip().lower()
    if run_again != 'y':
        print("Goodbye!")
        break
