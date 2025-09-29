"""
This module contains an exercise for 100 Days of Python
"""
import random
from hangman_words import word_list
import hangman_art

# 6 - let the player know how many lives left

word = list(random.choice(word_list))
length = len(word)
attempts = 6
game_over = False

placeholder = []
used_chars = []
for i in range(0, length):
    placeholder.append("_")

print(f"{hangman_art.logo3}\nThis is your word:")
print(''.join(placeholder))

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
            print(f"\nYou won!\n{hangman_art.logo2}")
        else:
            print("\nYou got one!\n")
            print(hangman_art.stages[attempts])
            print(''.join(placeholder))
    else:
        attempts -= 1
        print(hangman_art.stages[attempts])
        print(''.join(placeholder))
        if attempts == 0:
            game_over = True
            print(f"\nYou've been HUNG!\n The word was {''.join(word)}")
        else:
            print(f"Oops, try again! You've lost a life!\n Lives left: {attempts}")
            # These were here but do not belong anymore. What now ?
            # print(hangman_art.stages[attempts])
            # print(''.join(placeholder))

    used_chars.append(guess)
