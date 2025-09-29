"""
This module contains an exercise for 100 Days of Python
"""
import random

# 1 - use words from list
# 2 - use stages from file
# 3 - import the logo from art file
# 4 - verify already chosen letter
# 5 - let the player know he lost a life
# 6 - let the player know how many lives left

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']


word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
word = list(random.choice(word_list))
length = len(word)
attempts = 6
game_over = False

placeholder = []
used_chars = []
for i in range(0, length):
    placeholder.append("_")

print("Welcome to a game of Hangman!\nThis is your word:")
print(''.join(placeholder))

# Use a while loop to let the user guess again
while not game_over:
    guess = input("\nChoose a letter: ").lower()

    for i in range(0, length):
        if guess == word[i]:
            placeholder[i] = word[i]

    if guess in used_chars:
        print("Hey, you already told me that letter!")
    elif guess in placeholder:
        if "_" not in placeholder:
            game_over = True
            print("\nYou won! Great job!")
        else:
            print("\nYou got one!\n")
            print(stages[6 - attempts])
            print(''.join(placeholder))
    else:
        attempts -= 1
        print(stages[6 - attempts])
        print(''.join(placeholder))
        if attempts == 0:
            game_over = True
            print("\nYou've been HUNG!")
        else:
            print("Oops, try again!\n")
            print(stages[6 - attempts])
            print(''.join(placeholder))

    used_chars.append(guess)
