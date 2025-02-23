def display_inventory(inventory):
    """Displays the player's inventory with item counts and total count."""
    print("\nInventory:")
    item_total = 0
    for item, count in inventory.items():
        print(f"{count} {item if count == 1 else item + 's'}")  # Handles pluralization
        item_total += count
    print(f"Total number of items: {item_total}")

def add_to_inventory(inventory, loot):
    """Adds new items from loot (list) to the inventory (dictionary)."""
    for item in loot:
        inventory[item] = inventory.get(item, 0) + 1

# Predefined inventory
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

while True:
    # Display inventory
    display_inventory(inventory)

    # Allow user to add loot items
    loot = input("\nEnter loot items found (comma-separated, or 'none' to skip): ").strip().lower()
    
    if loot != "none":
        loot_list = [item.strip() for item in loot.split(",") if item.strip()]
        add_to_inventory(inventory, loot_list)

    # Ask user if they want to continue
    run_again = input("\nWould you like to add more loot? (y/n): ").strip().lower()
    if run_again != 'y':
        print("\nFinal Inventory:")
        display_inventory(inventory)
        print("Goodbye!")
        break
