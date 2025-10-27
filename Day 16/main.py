"""
This module contains an exercise for 100 Days of Python
"""
# Object
# Attributes - things that it has
# Methods - things that it can do
# Object -> Blueprint -> Class
# https://docs.python.org/3/library/turtle.html

# import another_module
# print(another_module.another_variable)
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)
my_screen.exitonclick()


