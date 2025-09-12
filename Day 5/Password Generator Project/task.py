"""
This module contains an exercise for 100 Days of Python
"""
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
char_type = ""
tray = []
total = nr_letters + nr_symbols + nr_numbers
if nr_letters > 0:
    tray.append("nr_letters")
if nr_symbols > 0:
    tray.append("nr_symbols")
if nr_numbers > 0:
    tray.append("nr_numbers")

# Debug
# Print(tray)

for i in range(1, total + 1):
    char_type = random.choice(tray)
    if char_type == "nr_letters":
        password += random.choice(letters)
        nr_letters -= 1
        if nr_letters == 0:
            tray.remove("nr_letters")

    if char_type == "nr_symbols":
        password += random.choice(symbols)
        nr_symbols -= 1
        if nr_symbols == 0:
            tray.remove("nr_symbols")

    if char_type == "nr_numbers":
        password += random.choice(numbers)
        nr_numbers -= 1
        if nr_numbers == 0:
            tray.remove("nr_numbers")

print(f"\nYour password is {password}")
