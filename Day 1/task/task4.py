"""
This module contains activities referencing 100 Days of Python course.
"""
# pylint: disable=invalid-name

# Python Variables
name = input("What is your name Sir?")

print("Hello " + name + ". Your name has " + str(len(name)) + " characters, right?")

name = "Jack"

print("Hello " + name + ". Your name has " + str(len(name)) + " characters, right?")

print(len(input("What is your name again?")))
