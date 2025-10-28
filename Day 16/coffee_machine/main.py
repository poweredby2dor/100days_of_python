"""
This module contains an exercise for 100 Days of Python
"""


from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
machine = CoffeeMaker()
menu = Menu()
cash_machine = MoneyMachine()


def refill_machine(machine_name):
    """
    Advanced Python - refill
    :param machine_name:
    :return:
    """
    print("Refilling machine...")
    for item in machine_name.resources:
        # Double them
        machine_name.resources[item] += machine_name.resources[item]


def use_machine():
    """
    Main function for Coffee Maker
    :return:
    """
    run_machine = True
    drink = None

    while run_machine:
        options = menu.get_items()
        choice = input(f"\nWhat would you like? /{options}:\n").lower()
        if choice == "off":
            run_machine = False
        elif choice == "report":
            machine.report()
            cash_machine.report()
        else:
            drink = menu.find_drink(choice)

        if drink:
            # Check resources
            if machine.is_resource_sufficient(drink):
                # Check money
                if cash_machine.make_payment(drink.cost):
                    # Do coffee
                    machine.make_coffee(drink)
                else:
                    if cash_machine.make_payment(drink.cost):
                        # Do coffee again
                        machine.make_coffee(drink)
            else:
                run_machine = False


# Advanced Python exercise
refill_machine(machine)

# Here runs the code
use_machine()
