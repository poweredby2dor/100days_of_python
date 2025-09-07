"""
This module contains an exercise for 100 Days of Python
"""


height = int(input("Welcome to the rollercoaster!\n What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    elif age > 60:
        print("You are a bit too old for this ride. I'm sorry.")
    else:
        print("Please pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")
