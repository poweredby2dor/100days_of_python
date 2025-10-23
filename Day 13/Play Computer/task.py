"""
This module contains an exercise for 100 Days of Python
"""


year = int(input("What's your year of birth?\n "))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")
