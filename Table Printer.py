def print_table(table):
    """Prints a list of lists as a neatly formatted table with right-aligned columns."""
    # Determine column widths
    col_widths = [max(len(item) for item in col) for col in table]

    # Transpose the table (switch rows and columns)
    for row in range(len(table[0])):
        for col in range(len(table)):
            print(table[col][row].rjust(col_widths[col]), end="  ")
        print()  # New line after each row

# Sample table data
table_data = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"]
]

# Print formatted table
print_table(table_data)
