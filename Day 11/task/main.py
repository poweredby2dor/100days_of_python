"""
This module contains an exercise for 100 Days of Python
"""

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 8, 9, 10, 10, 10, 10]
dealer = []
player = []


def start_game():
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n'\n")
    if play == "y":
        for i in range(0, 2):
            player.append(random.choice(cards))
            dealer.append(random.choice(cards))

        print(f"{logo}\nThank you for playing, let's go.\n Dealer has {dealer[0]} and [X]\n  You have {player[0]} and {player[1]}")
    elif play == "n":
        print("Feel free to return anytime.")
        exit()
    else:
        print("I'm sorry, I didn't catch that...")
        start_game()


def run_game():
    play = input(f"   Your score {sum(player)}, type 'y' to get another card, type 'n' to pass:\n")
    if play == "y":
        player.append(random.choice(cards))
        if sum(player) > 21:
            print("Player loses, house wins.")
            # Restart game
        elif sum(player) == 21 and sum(dealer) == 21:
            print("Draw!")
            # Restart game
        elif sum(player) == 21 and sum(dealer) != 21:
            # Evaluate if the dealer can draw safely?
            print("Blackjack! Player wins.")
            # Restart game
    elif play == "n":
        # Evaluate cards
        print("Evaluate cards")
    else:
        print("I'm sorry, I didn't catch that...")
        run_game()


# Code runs here
start_game()
run_game()
