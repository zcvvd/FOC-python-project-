# search.py
# Searches the inventory for medicines that match a keyword
# (looks in both the medicine name and the brand name).

import display
import utils

def search(stock):   # <-- parameter renamed from 'inventory' to 'stock'
    """Let the user search for medicines by name or brand."""
    print("\n=== Search Medicine ===")
    keyword = utils.get_non_empty_string("Enter medicine name or brand to search: ").lower()
    matches = []
    for med in stock:   # use stock
        if keyword in med["name"].lower() or keyword in med["brand"].lower():
            matches.append(med)

    if len(matches) == 0:
        print("No matching medicines found.")
    else:
        print(f"\nFound {len(matches)} medicine(s):")
        display.show_all_medicines(matches)
    utils.wait_for_enter()
