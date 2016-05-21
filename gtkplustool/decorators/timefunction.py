# -*- coding: utf-8 -*-
from functools import wraps
import time

__author__ = 'xiaolong'


def timefunction(function):
    @wraps(function)
    def wrap(*args, **kw):
        time_before_execution = time.monotonic()
        result = function(*args, **kw)
        time_after_execution = time.monotonic()
        print('Function', function.__name__, 'needed', (time_after_execution - time_before_execution) * 1000, 'ms to finish.')
        return result
    return wrap
