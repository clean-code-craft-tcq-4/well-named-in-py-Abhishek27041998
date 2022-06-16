# This file contains the test for utility functions related to
# color coding like getting name from color pair and vice versa
from color_code_utils import get_pair_number_from_color, \
    get_color_from_pair_number


def test_number_to_pair(pair_number, expected_major_color,
                        expected_minor_color):
    major_color, minor_color = get_color_from_pair_number(pair_number)

    assert(major_color == expected_major_color)
    assert(minor_color == expected_minor_color)


def test_pair_to_number(major_color, minor_color, expected_pair_number):
    pair_number = get_pair_number_from_color(major_color, minor_color)
    assert(pair_number == expected_pair_number)
