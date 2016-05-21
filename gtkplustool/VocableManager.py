# -*- coding: utf-8 -*-
from AppSettings import AppSettings
from FileManager import FileManager
from decorators.changesvocables import changesvocables
from exceptions.DuplicateVocableException import DuplicateVocableException
from exceptions.UnknownVocableException import UnknownVocableException

__author__ = 'xiaolong'


class VocableManager:

    vocables = []
    search_result = []
    vocables_changed = False

    test_counter = 0
    test_call_counter = 0

    def __init__(self):
        pass

    @classmethod
    @changesvocables
    def remove_vocable(cls, vocable):
        VocableManager.test_call_counter += 1
        if vocable in VocableManager.vocables:
            VocableManager.test_counter += 1
            VocableManager.vocables.remove(vocable)
            # del vocable
        else:
            print(vocable)
            raise UnknownVocableException('Vocable not found.')
        # VocableManager.vocables_changed = True

    @classmethod
    @changesvocables
    def remove_vocable_by_index(cls, index):
        del VocableManager.vocables[index]
        # VocableManager.vocables_changed = True

    @classmethod
    @changesvocables
    def add_vocable(cls, vocable):
        if vocable not in VocableManager.vocables:
            VocableManager.vocables.append(vocable)
        else:
            raise DuplicateVocableException('The vocable already exists.')
        # VocableManager.vocables_changed = True

    @classmethod
    def set_search_result(cls, search_result):
        """"This is a necessary setter. Other objects might listen for changes and need to be notified on changes."""
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
        xml_file_path = AppSettings.get_setting_by_name(AppSettings.XML_VOCABLE_FILE_PATH_SETTING_NAME)
        xsd_file_path = AppSettings.get_setting_by_name(AppSettings.XSD_VOCABLE_FILE_PATH_SETTING_NAME)

        VocableManager.vocables = FileManager.load_vocables(xml_file_path, xsd_file_path)
        VocableManager.search_result = VocableManager.vocables

    @classmethod
    def save_vocables(cls, vocable_list):
        xml_file_path = AppSettings.get_setting_by_name(AppSettings.XML_VOCABLE_FILE_PATH_SETTING_NAME)
        xsd_file_path = AppSettings.get_setting_by_name(AppSettings.XSD_VOCABLE_FILE_PATH_SETTING_NAME)
        FileManager.save_vocables(vocable_list, xml_file_path, xsd_file_path)
