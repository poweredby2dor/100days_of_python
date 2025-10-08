"""
This module contains an exercise for 100 Days of Python
"""

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer = []
player = []
player_wants_to_play = False


def start_game(first_game):
    global player_wants_to_play
    if first_game:
        play = input("\n\nDo you want to play a game of Blackjack? Type 'y' or 'n'\n")
    else:
        play = input("\n\nDo you want to play another game of Blackjack? Type 'y' or 'n'\n")
    if play == "y":
        player_wants_to_play = True
        for i in range(0, 2):
            player.append(random.choice(cards))
            dealer.append(random.choice(cards))

        # Natural Blackjack
        check_cards(True)

        print(f"{logo}\nThank you for playing, let's go.\n\n Dealer has [{dealer[0]}] and [X]\n  You have [{player[0]}] and [{player[1]}].")
    elif play == "n":
        print("Feel free to return anytime.")
        player_wants_to_play = False
    else:
        print("I'm sorry, I didn't catch that...")
        start_game(first_game)


def run_game():
    check_cards(False)

    play = input(f"   Your score {sum(player)}, type 'y' to get another card, type 'n' to pass:\n")
    if play == "y":
        player.append(random.choice(cards))
        if sum(player) > 21:
            print(f"{sum(player)} points, player loses, house wins.")
        elif sum(player) == 21 and sum(dealer) < 21:
            # TODO Evaluate if the dealer can draw safely?
            print("Blackjack! Player wins.")
        elif sum(dealer) == 21:
            print("House has Blackjack!")

        if sum(player) > 21 or (sum(player) == 21 and sum(dealer) < 21) or sum(dealer) > 21:
            show_cards(and_restart=True)

    elif play == "n":
        evaluate_cards()
    else:
        print("I'm sorry, I didn't catch that...")
        run_game()


def restart_game():
    global player_wants_to_play
    player_wants_to_play = False
    player.clear()
    dealer.clear()
    start_game(first_game=False)


def evaluate_cards():
    if sum(player) > sum(dealer):
        show_cards(False)
        print(f"Player wins!\n With {sum(player)} points versus {sum(dealer)} points on the house.\n\n\n")
    elif sum(player) == sum(dealer):
        show_cards(False)
        print(f"It's a draw.\n\n\n")
    else:
        show_cards(False)
        print(f"House wins with {sum(dealer)} points. Better luck next time.\n\n\n")

    restart_game()


def check_cards(natural_blackjack):
    if sum(player) == 21 and sum(dealer) == 21:
        print("Push. It's a tie.")
    elif sum(player) == 21:
        if natural_blackjack:
            print("Natural Blackjack!")
        else:
            print("Blackjack! you are lucky!")
    elif sum(dealer) == 21:
        if natural_blackjack:
            print("House wins with Natural Blackjack")
        else:
            print("House wins.")

    if sum(player) == 21 or sum(dealer) == 21:
        show_cards(and_restart=True)


def show_cards(and_restart):
    print(f"House had {dealer} and you had {player}\n")
    if and_restart:
        restart_game()


# Code runs here
start_game(first_game=True)
while player_wants_to_play:
    run_game()
