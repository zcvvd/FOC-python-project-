# restock.py
# Handles adding stock from a supplier – either topping up an existing medicine
# or adding a brand new one. It also creates a restock note.
# Restock note uses f‑string alignment for columns.

import display
import utils
import inventory

def restock(stock):   # <-- parameter renamed from 'inventory' to 'stock'
    """Restock medicines from a supplier. Can restock existing or add new medicines."""
    print("\n=== Restock Medicine ===")
    restock_cart = []

    while True:
        print("\n1. Restock an existing medicine")
        print("2. Add a new medicine")
        print("0. Done / finish restocking")
        option = utils.get_positive_int("What would you like to do? ")

        if option == 0:
            break
        elif option == 1:
            # --- Restock existing medicine ---
            medicine = display.choose_medicine(stock)   # use stock
            if medicine is None:
                continue

            # Ask for unit type
            unit = None
            while True:
                try:
                    choice = int(input("Choose unit (1 = Tablet, 2 = Strip): "))
                    if choice == 1:
                        unit = "Tablet"
                        break
                    elif choice == 2:
                        unit = "Strip"
                        break
                    else:
                        print("Enter 1 or 2.")
                except ValueError:
                    print("Invalid input.")

            if unit == "Strip" and medicine["tablets_per_strip"] == 0:
                print("Error: tablets per strip is 0. Cannot restock in strips.")
                continue

            # Quantity can be any positive number
            while True:
                try:
                    quantity = int(input(f"How many {unit}s to add? "))
                    if quantity <= 0:
                        print("Enter a positive number.")
                    else:
                        break
                except ValueError:
                    print("Please enter a whole number.")

            unit_price = medicine["rate_tablet"] if unit == "Tablet" else medicine["rate_strip"]
            line_total = quantity * unit_price
            tablets_added = quantity if unit == "Tablet" else quantity * medicine["tablets_per_strip"]

            restock_cart.append({
                "medicine": medicine,
                "quantity": quantity,
                "unit": unit,
                "unit_price": unit_price,
                "total": line_total,
                "tablets_added": tablets_added
            })

            print(f"Added {quantity} {unit} of {medicine['name']}. Cost: Rs.{line_total:.2f}")

        elif option == 2:
            # --- Add a brand new medicine ---
            print("\n--- Enter details for the new medicine ---")
            name = utils.get_non_empty_string("Medicine name: ")
            brand = utils.get_non_empty_string("Brand: ")
            initial_qty = utils.get_positive_int("Initial quantity (tablets): ")
            tab_price = utils.get_positive_float("Price per tablet (Rs): ")
            strip_price = utils.get_positive_float("Price per strip (Rs): ")
            tabs_per_strip = utils.get_positive_int("Tablets per strip: ")

            new_medicine = {
                "name": name,
                "brand": brand,
                "quantity": initial_qty,
                "rate_tablet": tab_price,
                "rate_strip": strip_price,
                "tablets_per_strip": tabs_per_strip
            }
            stock.append(new_medicine)   # use stock

            restock_cart.append({
                "medicine": new_medicine,
                "quantity": initial_qty,
                "unit": "Tablet",
                "unit_price": tab_price,
                "total": initial_qty * tab_price,
                "tablets_added": initial_qty
            })
            print(f"New medicine '{name}' added to inventory.")

        else:
            print("Invalid option. Please choose 0, 1 or 2.")
            continue

        if input("Add another item to the restock? (y/n): ").lower() != "y":
            break

    if len(restock_cart) == 0:
        print("No items selected. Restock cancelled.")
        return

    supplier_name = utils.get_non_empty_string("Supplier name: ")

    # ---- Display restock note on screen with aligned columns ----
    print("\n" + "=" * 65)
    print("RESTOCK NOTE")
    print(f"Supplier: {supplier_name}")
    print(f"Date: {utils.current_datetime_string()}")
    print("-" * 65)
    print(f"{'Item':<20} {'Qty':>4} {'Unit':<8} {'Price':>8} {'Total':>8}")
    print("-" * 65)

    grand_total = 0.0
    for item in restock_cart:
        grand_total += item["total"]
        print(f"{item['medicine']['name']:<20} {item['quantity']:>4} {item['unit']:<8} "
              f"{item['unit_price']:>8.2f} {item['total']:>8.2f}")

    print("-" * 65)
    print(f"{'Grand Total':>44} {grand_total:>8.2f}")
    print("=" * 65)

    if input("Confirm restock? (y/n): ").lower() != "y":
        print("Restock cancelled.")
        return

    # ---- Increase stock quantities ----
    for item in restock_cart:
        item["medicine"]["quantity"] += item["tablets_added"]
    inventory.save_inventory(stock)   # save the stock list using the module

    # ---- Save restock note to file (same aligned format) ----
    note_filename = utils.make_unique_filename("restock")
    try:
        with open(note_filename, "w") as f:
            f.write("=" * 65 + "\n")
            f.write("RESTOCK NOTE\n")
            f.write(f"Supplier: {supplier_name}\n")
            f.write(f"Date: {utils.current_datetime_string()}\n")
            f.write("-" * 65 + "\n")
            f.write(f"{'Item':<20} {'Qty':>4} {'Unit':<8} {'Price':>8} {'Total':>8}\n")
            f.write("-" * 65 + "\n")
            for item in restock_cart:
                f.write(f"{item['medicine']['name']:<20} {item['quantity']:>4} {item['unit']:<8} "
                        f"{item['unit_price']:>8.2f} {item['total']:>8.2f}\n")
            f.write("-" * 65 + "\n")
            f.write(f"{'Grand Total':>44} {grand_total:>8.2f}\n")
            f.write("=" * 65 + "\n")
        print(f"Restock note saved as: {note_filename}")
    except Exception as error:
        print("Error saving restock file:", error)

    utils.wait_for_enter()
