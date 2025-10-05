"""
This module contains an exercise for 100 Days of Python
"""
from art import logo

print(logo)
loop = True
value1 = int(input("Provide a first number:\n "))

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

while loop:
    operand = input("What operation do you want to execute? Type a symbol + - * /\n")
    while operand not in operations.keys():
        operand = input("What operation do you want to execute? Type a symbol + - * /\n")
    value2 = int(input("Provide a second number:\n "))
    value1 = operations[operand](value1, value2)
    if input(f"Result is {value1}. Do you want to make another calculation? Type y or n:\n").lower() == "n":
        loop = False
        print("Thank you.")
