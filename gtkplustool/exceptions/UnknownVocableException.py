# -*- coding: utf-8 -*-
__author__ = 'xiaolong'


class UnknownVocableException(BaseException):
    def __init__(self, message):
        super().__init__(message)
