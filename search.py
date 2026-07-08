# sales.py
# Handles the complete sale process: building a cart, applying discounts,
# updating stock, and printing / saving an invoice.
# Invoice uses f‑string formatting (e.g., :>8) for neat columns.

import display
import utils
import inventory

def calculate_discount(quantity, unit_type, line_total):
    """Give 5% off when the customer buys 2 or more strips of the same medicine."""
    if unit_type == "Strip" and quantity >= 2:
        return line_total * 0.05
    return 0.0

def sell(stock):   # <-- parameter renamed from 'inventory' to 'stock'
    """Run a sale for a customer. One transaction can contain many different medicines."""
    print("\n=== Sell Medicine ===")
    cart = []

    # ---- Add items to the cart ----
    while True:
        medicine = display.choose_medicine(stock)   # use stock
        if medicine is None:
            break

        if medicine["quantity"] == 0:
            print("This medicine is out of stock.")
            continue

        # Ask whether the customer wants Tablets or Strips
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

        # Figure out how many units can be sold
        if unit == "Tablet":
            max_available = medicine["quantity"]
        else:
            if medicine["tablets_per_strip"] == 0:
                print("Error: tablets per strip is zero. Skipping this medicine.")
                continue
            max_available = medicine["quantity"] // medicine["tablets_per_strip"]

        print(f"Available: {max_available} {unit}(s)")

        # Ask for the quantity and check it's valid
        while True:
            try:
                quantity = int(input(f"How many {unit}s? "))
                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                elif quantity > max_available:
                    print(f"Not enough stock. Maximum available is {max_available}.")
                else:
                    break
            except ValueError:
                print("Please enter a whole number.")

        # Calculate costs and discount
        unit_price = medicine["rate_tablet"] if unit == "Tablet" else medicine["rate_strip"]
        subtotal = quantity * unit_price
        discount_amount = calculate_discount(quantity, unit, subtotal)
        net = subtotal - discount_amount
        tablets_used = quantity if unit == "Tablet" else quantity * medicine["tablets_per_strip"]

        cart.append({
            "medicine": medicine,
            "quantity": quantity,
            "unit": unit,
            "unit_price": unit_price,
            "subtotal": subtotal,
            "discount": discount_amount,
            "net": net,
            "tablets_used": tablets_used
        })

        print(f"Added {quantity} {unit} of {medicine['name']}. Net: Rs.{net:.2f}")
        if input("Add another medicine? (y/n): ").lower() != "y":
            break

    if len(cart) == 0:
        print("No items selected. Sale cancelled.")
        return

    customer_name = utils.get_non_empty_string("Customer name: ")

    # ---- Print invoice on the screen with aligned columns ----
    print("\n" + "=" * 65)
    print("                       SALES INVOICE")
    print("=" * 65)
    print(f" Customer : {customer_name}")
    print(f" Date     : {utils.current_datetime_string()}")
    print("-" * 65)
    # Column headers with alignment
    print(f"{'Item':<20} {'Qty':>3}  {'Unit':<8} {'Price':>7} {'Amount':>9} {'Disc':>8} {'Net':>8}")
    print("-" * 65)

    total_subtotal = 0.0
    total_discount = 0.0
    for item in cart:
        total_subtotal += item["subtotal"]
        total_discount += item["discount"]
        print(f"{item['medicine']['name']:<20} {item['quantity']:>3}  {item['unit']:<8} "
              f"{item['unit_price']:>7.2f} {item['subtotal']:>9.2f} {item['discount']:>8.2f} {item['net']:>8.2f}")

    print("-" * 65)
    print(f"{'Subtotal':>53} {total_subtotal:>9.2f}")
    print(f"{'Discount':>53} {total_discount:>9.2f}")
    print(f"{'TOTAL':>53} {total_subtotal - total_discount:>9.2f}")
    print("=" * 65)

    if input("Confirm sale? (y/n): ").lower() != "y":
        print("Sale cancelled.")
        return

    # ---- Update stock ----
    for item in cart:
        item["medicine"]["quantity"] -= item["tablets_used"]
    inventory.save_inventory(stock)   # save the stock list using the module

    # ---- Save invoice to file (same aligned format) ----
    invoice_filename = utils.make_unique_filename("sale")
    try:
        with open(invoice_filename, "w") as f:
            f.write("=" * 65 + "\n")
            f.write("                       SALES INVOICE\n")
            f.write("=" * 65 + "\n")
            f.write(f" Customer : {customer_name}\n")
            f.write(f" Date     : {utils.current_datetime_string()}\n")
            f.write("-" * 65 + "\n")
            f.write(f"{'Item':<20} {'Qty':>3}  {'Unit':<8} {'Price':>7} {'Amount':>9} {'Disc':>8} {'Net':>8}\n")
            f.write("-" * 65 + "\n")
            for item in cart:
                f.write(f"{item['medicine']['name']:<20} {item['quantity']:>3}  {item['unit']:<8} "
                        f"{item['unit_price']:>7.2f} {item['subtotal']:>9.2f} {item['discount']:>8.2f} {item['net']:>8.2f}\n")
            f.write("-" * 65 + "\n")
            f.write(f"{'Subtotal':>53} {total_subtotal:>9.2f}\n")
            f.write(f"{'Discount':>53} {total_discount:>9.2f}\n")
            f.write(f"{'TOTAL':>53} {total_subtotal - total_discount:>9.2f}\n")
            f.write("=" * 65 + "\n")
        print(f"Invoice saved as: {invoice_filename}")
    except Exception as error:
        print("Error saving invoice file:", error)

    utils.wait_for_enter()
