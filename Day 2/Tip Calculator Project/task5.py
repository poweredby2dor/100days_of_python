"""
This module contains an exercise for 100 Days of Python
"""

# Tip Calculator

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15 percent? "))
people = int(input("How many people will split this bill? "))

total = round(total * (tip / 100 + 1) / people, 2)

print(f"Each person should pay: $ {total}")
