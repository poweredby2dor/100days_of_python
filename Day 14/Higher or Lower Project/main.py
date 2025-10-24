"""
This module contains an exercise for 100 Days of Python
"""


from art import logo, vs
import game_data
import random
game_on = True
influencers = game_data.data.copy()


def compare(play_game):
    """
    Main function
    :param play_game:
    :return:
    """
    score = 0
    last_choice = {}

    while play_game:
        choice2 = random.choice(influencers)
        influencers.remove(choice2)
        if score == 0:
            choice1 = random.choice(influencers)
            influencers.remove(choice1)
            last_choice = ask_user(choice1, choice2)
        else:
            last_choice = ask_user(last_choice, choice2)

        if last_choice == "exit":
            print(f"Your score: {score}")
            play_game = False
        else:
            score += 1

        if not influencers:
            print(f"Your score: {score}")
            play_game = False


def ask_user(a, b):
    """
    User input function
    :param a:
    :param b:
    :return:
    """
    print(f"Compare A: {a["name"]}, a/n {a["description"]}, from {a["country"]}")
    print(vs)
    print(f"Against B: {b["name"]}, a/n {b["description"]}, from {b["country"]}")
    choice = input("Who has more followers? Type 'A' or 'B'").lower()

    if choice == "a":
        if a["follower_count"] > b["follower_count"]:
            print(f"\nYou are right, {a["name"]} has {a["follower_count"]} million followers, more than {b["name"]} with {b["follower_count"]} millions.\n")
            return a
        else:
            print(f"\nYou are wrong, {a["name"]} with {a["follower_count"]} million followers has less than {b["name"]} with {b["follower_count"]} millions.\n")
            return "exit"
    else:
        if b["follower_count"] > a["follower_count"]:
            print(f"\nYou are right, {b["name"]} has {b["follower_count"]} million followers, more than {a["name"]} with {a["follower_count"]} millions.\n")
            return b
        else:
            print(f"\nYou are wrong, {b["name"]} with {b["follower_count"]} million followers has less than {a["name"]} with {a["follower_count"]} millions.\n")
            return "exit"


print(logo)
compare(game_on)
