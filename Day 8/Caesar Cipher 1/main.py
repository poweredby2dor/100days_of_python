"""
This module contains an exercise for 100 Days of Python
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount, result=""):
    for letter in original_text:
        result += alphabet[(alphabet.index(letter) + shift_amount) % len(alphabet)]

    print(result)


encrypt(original_text=text, shift_amount=shift)
