"""
This module contains an exercise for 100 Days of Python
"""


from art import logo
import random
attempts = 0
the_number = random.randint(1, 100)

print(logo)

print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")

difficulty = input("  Choose a difficulty. Type 'easy' or 'hard'\n  ").lower()
while not difficulty == "easy" and not difficulty == "hard":
    difficulty = input("Sorry, I did not understand you. 'easy' or 'hard'?\n").lower()

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

while attempts:
    guess = int(input("Make a guess: "))
    attempts -= 1
    if guess == the_number:
        print(f"\nYou guess it! Great work, you played on difficulty {difficulty} and had {attempts} tries left")
        exit()
    elif guess < the_number:
        print("Too low!")
    else:
        print("Too high!")
