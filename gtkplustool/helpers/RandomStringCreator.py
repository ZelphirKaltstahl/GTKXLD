# -*- coding: utf-8 -*-
import random
import string

__author__ = 'xiaolong'


class RandomStringCreator:
    def __init__(self):
        pass

    @classmethod
    def randomword(cls, length):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(length))
