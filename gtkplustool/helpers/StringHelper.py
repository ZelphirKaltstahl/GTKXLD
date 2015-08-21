# -*- coding: utf-8 -*-
from math import log10

__author__ = 'xiaolong'


def get_leading_zero_number_string(number, length):
    """
    This function adds as many leading zeros to a number's string representation as are necessary to reach the specified length and returns this string representation.

    :param number: the number, which will be converted to a string, to which the leading zeros will be added
    :param length: the length the string representation of the number shall have, when the leading zeros have been added
    """
    return ('{0:0' + str(length) + 'd}').format(number)


def len_of_number(number):
    """
    This function returns the length of a number to base 10.

    :param number: the number of which the length will be returned
    :return: the length of the given number to base 10
    """
    return int(log10(number) + 1)
