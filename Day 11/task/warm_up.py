"""
This module contains an exercise for 100 Days of Python
"""

import random

cards = [11, 2, 3, 4, 5, 6, 8, 9, 10, 10, 10, 10]

dealer = []
player = []

for i in range(0, 2):
    dealer.append(random.choice(cards))
    player.append(random.choice(cards))

number = sum(player)

print(number)
