"""
This module contains an exercise for 100 Days of Python
"""


from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def use_machine():
    """
    Main function for Coffee Maker
    :return:
    """
    machine = CoffeeMaker()
    menu = Menu()
    cash_machine = MoneyMachine()

    choice = input("\nWhat would you like? (espresso/latte/cappuccino):\n").lower()
    drink = menu.find_drink(choice)

    if choice == "report":
        machine.report()
        cash_machine.report()
        use_machine()
    elif drink:
        # Check resources
        if machine.is_resource_sufficient(drink):
            # Check money
            cash_machine.make_payment(drink.cost)
        # Do coffee
        print(choice)


# Here runs the code
use_machine()
