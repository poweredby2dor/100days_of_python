"""
This module contains an exercise for 100 Days of Python
"""


def is_prime(num):
    if num == 1:
        prime = False
        return prime
    else:
        prime = True
    counter = num - 1
    while prime and counter > 1:
        if num % counter == 0:
            prime = False
        else:
            counter -= 1

    return prime


# Insert any number here to test
print(is_prime(1))
