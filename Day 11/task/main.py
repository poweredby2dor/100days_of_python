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

        # Dealer's turn
        dealer_draws(True)

        if sum(player) > 21 and 11 in player:
            print("###\nDEBUG\n###")

        if sum(player) > 21:
            print(f"{sum(player)} points, player loses, house wins.")
        elif sum(player) == 21 and sum(dealer) < 21:
            print("Blackjack! Player wins.")
        elif sum(dealer) == 21:
            print("House has Blackjack!")
        elif sum(dealer) > 21:
            print(f"You win with {sum(player)} points. House went over.")

        if sum(player) > 21 or (sum(player) == 21 and sum(dealer) < 21) or sum(dealer) > 21:
            show_cards(and_restart=True)

    elif play == "n":
        dealer_draws(False)
        evaluate_cards()
    else:
        print("I'm sorry, I didn't catch that...")
        run_game()


def restart_game():
    """
    Restarts the game by clearing cards and calling the start_game function
    :return:
    """
    global player_wants_to_play
    player_wants_to_play = False
    player.clear()
    dealer.clear()
    start_game(first_game=False)


def evaluate_cards():
    """
    Evaluates cards and determines who has more points
    :return:
    """
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
    """
    Prints cards for both player and dealer.
    :param and_restart: boolean to call the restart_game function
    :return:
    """
    print(f"House had {dealer} and you had {player}\n")
    if and_restart:
        restart_game()


def dealer_draws(also_player):
    """
    Function to check if the dealer can draw a card. Print differs if the player also has received a card.
    :param also_player: boolean to know if the player also received a card
    :return:
    """
    if sum(dealer) < 17 and sum(player) <= 21:
        dealer.append(random.choice(cards))
        if also_player:
            print("Dealer gives you a card and also deals a card to the house.")
        else:
            print("Dealer deals a card to the house.")
    elif also_player:
        print("Dealer gives you a card, then stands.")
    else:
        print("Dealers stands.")


# Code runs here
start_game(first_game=True)
while player_wants_to_play:
    run_game()
