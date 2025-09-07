"""
This module contains an exercise for 100 Days of Python
"""


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

"""
small pizza 15
medium 20
large 25
small pepperoni +2
medium or large pepperoni +3
extra cheese +1
"""

if size == "s":
    bill = 15
    if pepperoni == "y":
        bill += 2
elif size == "m":
    bill = 20
    if pepperoni == "y":
        bill += 3
else:
    bill = 25
    if pepperoni == "y":
        bill += 3

if extra_cheese == "y":
    bill += 1

print(f"your final bill is ${bill}")