def rotate_grid(grid):
    """Rotates a 2D grid 90 degrees clockwise and prints the result."""
    rows = len(grid)
    cols = len(grid[0])

    for col in range(cols):
        for row in range(rows - 1, -1, -1):  # Iterate from bottom to top
            print(grid[row][col], end="")
        print()  # Move to the next line

# Predefined character grid
grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]

while True:
    print("\nRotated Grid Output:\n")
    rotate_grid(grid)

    # Ask the user if they want to see it again
    run_again = input("\nWould you like to rotate again? (y/n): ").strip().lower()
    if run_again != 'y':
        print("Goodbye!")
        break
