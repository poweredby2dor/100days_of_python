"""
This module contains an exercise for 100 Days of Python
"""
import art

bidders = {}
run_input = True

print(art.logo)

while run_input:
    name = input("Tell me your name:\n")
    offer = int(input("Tell me your bid:\n"))
    bidders[name] = offer
    if input("Is there another bidder?\n").lower() == "no":
        run_input = False

winner = max(bidders, key=bidders.get)

print(f"The bid's winner is {winner} with a bid of {bidders[winner]}$")
