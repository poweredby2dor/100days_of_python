"""
This module contains an exercise for 100 Days of Python
"""
import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = ""


def caesar(original_text, shift_amount, encode_decode, cipher=""):
    if encode_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            cipher += alphabet[(alphabet.index(letter) + shift_amount) % len(alphabet)]
        else:
            cipher += letter

    print(f"Here is the {encode_decode}d result: {cipher}")


print(art.logo)

while direction != "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_decode=direction)

    if input("Type yes if you want to go again.\nOtherwise type no\n") == "no":
        direction = "no"
