# -*- coding: utf-8 -*-
__author__ = 'xiaolong'


class DuplicateVocableException(BaseException):
    def __init__(self, message):
        super().__init__(message)
