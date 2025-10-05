"""
This module contains an exercise for 100 Days of Python
"""


def format_name(f_name, l_name):
    """
    Take a first and last name and format it to return
    the title case version of the name
    :param f_name: first name
    :param l_name: last name
    :return: a string containing new first and last name
    """
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)



