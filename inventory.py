# display.py
# Handles showing the inventory on the screen and letting the user choose one medicine.
# No fancy alignment – just clean, readable text.

def show_all_medicines(inventory):
    """Display a simple table of every medicine in stock."""
    if len(inventory) == 0:
        print("\nNo medicines in stock.")
        return

    print("\n--- Medicine List ---")
    for index, med in enumerate(inventory, 1):
        # Print each medicine on one line with its details
        print(f"{index}. {med['name']}  |  {med['brand']}  |  Stock: {med['quantity']}  |  "
              f"Tab: Rs.{med['rate_tablet']}  |  Strip: Rs.{med['rate_strip']}  |  "
              f"Tabs/Strip: {med['tablets_per_strip']}")

def choose_medicine(inventory):
    """
    Show the table and ask the user to pick a medicine by its number.
    Returns the chosen medicine dictionary, or None if they cancel.
    """
    show_all_medicines(inventory)
    if len(inventory) == 0:
        return None

    while True:
        try:
            number = int(input("\nSelect medicine number (0 to cancel): "))
            if number == 0:
                return None
            if 1 <= number <= len(inventory):
                return inventory[number - 1]
            print("Number out of range. Try again.")
        except ValueError:
            print("Please enter a valid whole number.")