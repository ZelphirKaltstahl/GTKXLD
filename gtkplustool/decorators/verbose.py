# -*- coding: utf-8 -*-
__author__ = 'xiaolong'


def verbose(original_function):
    # make a new function that prints a message when original_function starts and finishes
    def new_function(*args, **kwargs):
        print("Entering", original_function.__name__)
        original_function(*args, **kwargs)
        print("Exiting ", original_function.__name__)

    return new_function
