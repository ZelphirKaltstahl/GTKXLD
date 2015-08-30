# -*- coding: utf-8 -*-
from FileManager import FileManager

__author__ = 'xiaolong'


class VocableManager:

    vocables = []
    search_result = []

    def __init__(self):
        pass

    @classmethod
    def remove_vocable(cls, vocable):
        VocableManager.vocables.remove(vocable)
        del vocable

    @classmethod
    def remove_vocable_by_index(cls, index):
        del VocableManager.vocables[index]

    @classmethod
    def add_vocable(cls, vocable):
        VocableManager.vocables.append(vocable)

    @classmethod
    def set_search_result(cls, search_result):
        VocableManager.search_result = search_result

    @classmethod
    def get_search_result(cls):
        return VocableManager.search_result

    @classmethod
    def get_search_result_vocable(cls, index):
        if index is not None and index >= 0:
            return VocableManager.search_result[index]
        return None

    @classmethod
    def load_vocables(cls):
        VocableManager.vocables = FileManager.load_vocables()
        VocableManager.search_result = VocableManager.vocables


