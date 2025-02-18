def collatz(number):
    """Applies the Collatz sequence rule to a given number."""
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

def get_valid_integer():
    """Prompts the user for a valid integer input."""
    while True:
        try:
            return int(input("Enter a positive integer: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

while True:
    num = get_valid_integer()

    # Ensure the input is positive
    if num <= 0:
        print("Please enter a positive integer greater than zero.")
        continue

    print(f"\nCollatz sequence starting from {num}:")
    
    while num != 1:
        num = collatz(num)
        print(num)

    # Ask user if they want to run again
    run_again = input("\nWould you like to enter another number? (y/n): ").strip().lower()
    if run_again != 'y':
        print("Goodbye!")
        break
