# utils.py
# Small helper functions used by almost every other file.
# They handle user input, timestamps, unique filenames, and pauses.

import datetime
import random

def get_positive_int(prompt):
    """Keep asking until the user enters a whole number >= 0."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive number (or 0).")
            else:
                return value
        except ValueError:
            print("That doesn't look like a whole number. Try again.")

def get_positive_float(prompt):
    """Keep asking until the user enters a decimal number > 0."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than 0.")
            else:
                return value
        except ValueError:
            print("Please enter a number like 12.50.")

def get_non_empty_string(prompt):
    """Keep asking until the user types something (not just an empty line)."""
    while True:
        text = input(prompt)          # No .strip() – we keep spaces if typed
        if text:                      # Empty string means they pressed Enter immediately
            return text
        print("This cannot be empty. Please try again.")

def current_datetime_string():
    """Return current date and time as 'DD/MM/YYYY  HH:MM'."""
    now = datetime.datetime.now()
    return f"{now.day:02d}/{now.month:02d}/{now.year}  {now.hour:02d}:{now.minute:02d}"

def make_unique_filename(prefix):
    """Create a filename that won't clash with others (date + random number)."""
    date_part = datetime.datetime.now().strftime("%Y%m%d")
    random_part = random.randint(1000, 9999)
    return f"{prefix}_{date_part}_{random_part}.txt"

def wait_for_enter():
    """Pause the program until the user presses Enter."""
    input("\nPress Enter to continue...")