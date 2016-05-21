# -*- coding: utf-8 -*-
from functools import wraps
from VocableManager import VocableManager as VocMan

__author__ = 'xiaolong'


def changesvocables(function):
    @wraps(function)
    def wrapper(*args, **kw):
        result = function(*args, **kw)
        VocMan.vocables_changed = True
        return result
    return wrapper
