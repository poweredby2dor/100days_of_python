"""
This module contains an exercise for 100 Days of Python
"""

from menu import MENU, resources


def query_user():
    """
    Function to ask user what to order
    :return:
    """
    choice = input("\nWhat would you like? (expresso/latte/cappuccino):\n")

    if choice == "report":
        for item in resources:
            print(f"{item.capitalize()} left: {resources[item]}")
    while choice not in MENU:
        query_user()

    return choice, 0


def process_coins(product, old_cash):
    """
    Function to process coins based on order input
    :param product: what order to make
    :param old_cash:
    :return:
    """
    if product not in MENU:
        print("[E] Program error, exiting")
        exit()
    else:
        cost = MENU[product]["cost"]
        print(f"A {product.capitalize()} costs: ${cost}")

        cash = float(input("How many quarters? ")) * 0.25 + old_cash
        cash = float(input("How many dimes? ")) * 0.1 + cash
        cash = float(input("How many nickles? ")) * 0.05 + cash
        cash = float(input("How many pennies? ")) * 0.01 + cash

        if cash >= cost:
            process_order(product, cash - cost)
        else:
            choice = input(f"Sorry, that's not enough money. A {product.capitalize()} is {cost}. Please add another ${cost-cash}. Thank you.\nType 'refund' for a full refund.")
            if choice == "refund":
                print(f"Your money has been refunded: ${cash}")
            process_coins(product, cash)


def process_order(product, change):
    """
    Function to process product from materials
    :param product:
    :param change:
    :return:
    """
    # Stocks checking
    ingredient_empty = []
    levels = resources.copy()
    for item in MENU[product]["ingredients"]:
        if levels[item] >= MENU[product]["ingredients"][item]:
            levels[item] -= MENU[product]["ingredients"][item]
        else:
            ingredient_empty.append(item)

    if ingredient_empty:
        print(f"Sorry, machine needs refilling for the following: {ingredient_empty}")



    change = round(change, 2)
    if change > 0:
        print(f"Here is your ${change} in change. Here is your {product.capitalize()} ☕\n   Enjoy and have a nice day!")

    print(MENU[product]["ingredients"])



process_coins(*query_user())
