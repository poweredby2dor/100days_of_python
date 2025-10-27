"""
This module contains an exercise for 100 Days of Python
"""

from turtle import Turtle, Screen

so = Turtle()
so.shape("turtle")
so.color("coral")
so.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)
my_screen.exitonclick()


