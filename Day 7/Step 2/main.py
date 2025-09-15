"""
This module contains an exercise for 100 Days of Python
"""
import random

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
word = random.choice(word_list)
length = len(word)
word = list(word)

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("\nWelcome to Hangman. Choose a letter: ").lower()

# Create a display where the good letter is shown in the word
placeholder = []
for i in range(0, length):
    placeholder.append("_")
for i in range(0, length):
    if guess == word[i]:
        placeholder[i] = word[i]

placeholder = ''.join(placeholder)
print(placeholder)
