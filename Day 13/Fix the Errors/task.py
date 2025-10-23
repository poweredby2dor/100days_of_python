"""
This module contains an exercise for 100 Days of Python
"""


age = 0

try:
    age = int(input("How old are you?"))
except ValueError:
    print("Type using integers")
    age = int(input("How old are you?"))
except Exception:
    print("Welp")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
