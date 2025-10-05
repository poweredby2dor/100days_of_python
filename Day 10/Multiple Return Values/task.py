"""
This module contains an exercise for 100 Days of Python
"""

f_name = input("Please give me your First Name: ")
l_name = input("Please give me your Last Name: ")


def format_name(first, last):
    if first == "" or last == "":
        return "You did not provide valid inputs"
    formatted_f_name = first.title()
    formatted_l_name = last.title()
    return f"{formatted_f_name} {formatted_l_name}"


print(format_name(f_name, l_name))
