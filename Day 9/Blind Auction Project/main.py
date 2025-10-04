"""
This module contains an exercise for 100 Days of Python
"""
import art

bidders = {}
run_input = True

print(art.logo)

while run_input:
    name = input("Tell me your name:\n")
    offer = int(input("Tell me your bid:\n$"))
    bidders[name] = offer
    if input("Is there another bidder?\n").lower() == "no":
        run_input = False


def find_highest_bidder(bidding_dictionary):
    winner = max(bidding_dictionary, key=bidding_dictionary.get)
    print(f"\nThe bid's winner is {winner} with a bid of {bidding_dictionary[winner]}$")


find_highest_bidder(bidders)
