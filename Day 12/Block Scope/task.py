"""
This module contains an exercise for 100 Days of Python
"""


# There is no Block Scope in Python
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]


def create_enemy():
    new_enemy = ""

    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)
