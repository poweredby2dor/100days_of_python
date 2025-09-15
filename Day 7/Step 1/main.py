"""
This module contains an exercise for 100 Days of Python
"""
import random

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
word = random.choice(word_list)
length = len(word)

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
print(word)
guess = input("Welcome to Hangman. Choose a letter: ").lower()

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is, "Wrong" if it's not.
for letter in word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
