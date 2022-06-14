# This file contains formatted string as user manual guide
from config import *
from get_pair_number_from_color import get_pair_number_from_color


def color_pair_to_string(major_color, minor_color):
    return f'{major_color} {minor_color}'


def color_number_to_string(number):
    return f'{number}'


def print_user_reference_manual():
    print(" ----------------- "
          "PRINTING THE USER REFERENCE MANUAL FOR THE COLOR CODE "
          "-----------------\n")
    print("{:<15} {:<15} {:<5}".format('MAJOR_COLOR',
                                       'MINOR_COLOR',
                                       'NUMBER'))

    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            number = get_pair_number_from_color(major_color, minor_color)
            number = color_number_to_string(number)
            print("{:<15} {:<15} {:<5}".
                  format(major_color, minor_color, number))