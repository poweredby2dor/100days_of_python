"""
This module contains an exercise for 100 Days of Python
"""

first = input("Type your full name: ")

second = input("Type your significant others name: ")


def calculate_love_score(name1, name2):
    name = name1 + name2
    score1 = 0
    score2 = 0
    for letter in "true":
        score1 += name.count(letter)
    for letter in "love":
        score2 += name.count(letter)

    score = int("".join([str(score1), str(score2)]))

    print(f"Love Score = {score}")


calculate_love_score(first, second)
