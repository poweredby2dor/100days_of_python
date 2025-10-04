"""
This module contains an exercise for 100 Days of Python
"""


programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again",
}

# print(programming_dictionary["Bug"])

# Loop through a dictionary
for key in programming_dictionary:
    print(f"{key}: {programming_dictionary[key]}")
