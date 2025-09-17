"""
This module contains an exercise for 100 Days of Python
"""
import random

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
word = list(random.choice(word_list))
length = len(word)
attempts = length

placeholder = []
used_chars = []
for i in range(0, length):
    placeholder.append("_")

# to be removed
print(''.join(placeholder))

print("Welcome to a game of Hangman!")

# Use a while loop to let the user guess again
while attempts > 0:
    guess = input("\nChoose a letter: ").lower()

    for i in range(0, length):
        if guess == word[i]:
            placeholder[i] = word[i]

    if guess in used_chars:
        print("Hey, you already told me that letter!")
    elif guess in placeholder:
        print("You got one!\n\n\n\n\n")
        print(''.join(placeholder))
    else:
        attempts -= 1
        print("Oops, yry again!\n\n\n\n\n")
        print(''.join(placeholder))

    used_chars.append(guess)

else:
    print("You've been HUNG!")
