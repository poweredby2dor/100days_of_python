"""
This module contains an exercise for 100 Days of Python
"""


from art import logo
from random import randint
ATTEMPTS = 0
THE_NUMBER = randint(1, 100)

print(logo)
print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")

difficulty = input("  Choose a difficulty. Type 'easy' or 'hard'\n  ").lower()
while not difficulty == "easy" and not difficulty == "hard":
    difficulty = input("Sorry, I did not understand you. 'easy' or 'hard'?\n").lower()

if difficulty == "easy":
    ATTEMPTS = 10
elif difficulty == "hard":
    ATTEMPTS = 5

while ATTEMPTS:
    guess = int(input(f"You have {ATTEMPTS} tries left. Make a guess: "))
    ATTEMPTS -= 1
    if guess == THE_NUMBER:
        print(f"\nYou guess it! Great work, you played on difficulty {difficulty} and had {ATTEMPTS} tries left")
        exit()
    elif guess < THE_NUMBER:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"\nYou didn't guess. The number was {THE_NUMBER}")
