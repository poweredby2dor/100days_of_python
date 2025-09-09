"""
This module contains an exercise for 100 Days of Python
"""
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# rock wins against scissors;
# scissors win against paper;
# paper wins against rock;

choices = ["rock", "paper", "scissors"]
game_images = [rock, paper, scissors]
computer = random.randint(0, 2)

player = input("Welcome to Rock, Paper, Scissors!\n What do you choose? Type 1, for Rock, 2 for Paper or 3 for Scissors: ")
player = int(player) - 1

if 1 >= player <= 3:
    print(f"\nYou: {game_images[player]}")
    print(f"\nComputer choose: {game_images[computer]}")
# Catch typos
else:
    print("Please play fairly!")
    exit()

# Angela used a lot of comparisons between values, but it didn't look elegant. Maybe improve on her choice.
if choices[computer] == "rock" and choices[player] == "paper":
    print("Paper wins, you won!")
elif choices[computer] == "rock" and choices[player] == "scissors":
    print("Rock wins, you lost!")
elif choices[computer] == "scissors" and choices[player] == "paper":
    print("Scissors wins, you lost!")
elif choices[computer] == "scissors" and choices[player] == "rock":
    print("Rock wins, you won!")
elif choices[computer] == "paper" and choices[player] == "scissors":
    print("Scissors wins, you win!")
elif choices[computer] == "paper" and choices[player] == "rock":
    print("Paper wins, you lost!")
else:
    print("Draw, go again!")
