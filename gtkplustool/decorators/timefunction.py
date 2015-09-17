# -*- coding: utf-8 -*-
import functools
import time

__author__ = 'xiaolong'


def timefunction(f):
    @functools.wraps(f)
    def wrap(*args, **kw):
        time_before_execution = time.monotonic()
        result = f(*args, **kw)
        time_after_execution = time.monotonic()
        print('Function', f.__name__, 'needed', (time_after_execution - time_before_execution) * 1000, 'ms to finish.')
        return result
    return wrap
