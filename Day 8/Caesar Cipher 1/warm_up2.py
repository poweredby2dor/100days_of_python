"""
This module contains an exercise for 100 Days of Python
"""

age = input("How old are you, if I may ask?")


def life_in_weeks(years):
    left = (90 - int(years)) * 52
    print(f"You have {left} weeks left.")


life_in_weeks(age)
