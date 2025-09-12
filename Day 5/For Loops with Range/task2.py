"""
This module contains an exercise for 100 Days of Python
"""

# Read this line

for number in range(1, 100+1):
    if number % 3 == 0:
        if number % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
