# inventory.py
# Reads and writes the medicines.txt file.
# All other parts use these functions to get or update stock.
# We do NOT use .strip(). Instead we handle newlines carefully.

INVENTORY_FILE_NAME = "medicines.txt"

def load_inventory():
    """
    Read the medicines.txt file.
    Returns a list of dictionaries – one dictionary per medicine.
    If the file is missing, an empty list is returned.
    """
    inventory = []
    try:
        with open(INVENTORY_FILE_NAME, "r") as file:
            for line_number, line in enumerate(file, 1):
                # Remove the trailing newline character (and any carriage return)
                if line.endswith("\n"):
                    line = line[:-1]
                if line.endswith("\r"):
                    line = line[:-1]
                if len(line) == 0:     # skip empty lines
                    continue
                parts = line.split(",")
                if len(parts) != 6:    # we need exactly 6 pieces of information
                    print(f"Warning: line {line_number} has wrong number of columns. Skipping.")
                    continue
                try:
                    # Convert the text values to the correct types
                    medicine = {
                        "name": parts[0],
                        "brand": parts[1],
                        "quantity": int(parts[2]),
                        "rate_tablet": float(parts[3]),
                        "rate_strip": float(parts[4]),
                        "tablets_per_strip": int(parts[5])
                    }
                    inventory.append(medicine)
                except ValueError:
                    print(f"Warning: line {line_number} has wrong number format. Skipping.")
    except FileNotFoundError:
        print("medicines.txt not found. Starting with empty inventory.")
    return inventory

def save_inventory(inventory):
    """Save the current list of medicines back to the file."""
    try:
        with open(INVENTORY_FILE_NAME, "w") as file:
            for med in inventory:
                # Write each medicine as a comma‑separated line
                file.write(f"{med['name']},{med['brand']},{med['quantity']},"
                           f"{med['rate_tablet']},{med['rate_strip']},{med['tablets_per_strip']}\n")
    except Exception as error:
        print("Error saving inventory:", error)
