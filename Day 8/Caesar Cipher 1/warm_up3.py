"""
This module contains an exercise for 100 Days of Python
"""

name = input("Hello, what is your name dear Sir ?")

city = input("Where are you from ?")


def greet(caller, location):
    print(f"Hello {caller} from {location}")


greet(name, city)
