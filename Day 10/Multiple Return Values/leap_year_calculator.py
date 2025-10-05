"""
This module contains an exercise for 100 Days of Python
"""

query = int(input("Provide a year to be checked if it is a leap year or not:\n"))


def is_leap_year(year):
    answer = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                answer = True
        else:
            answer = True
    else:
        answer = False

    return answer


if is_leap_year(query):
    print(f"{query} is a leap year.")
else:
    print(f"{query} is a not leap year.")
