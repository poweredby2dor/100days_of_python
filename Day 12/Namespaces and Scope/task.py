"""
This module contains an exercise for 100 Days of Python
"""


enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Global Scope
player_health = 10


# Local Scope
def drink_potion():
    potion_strength = 2
    global player_health
    player_health = player_health + potion_strength
    print(player_health)


drink_potion()
