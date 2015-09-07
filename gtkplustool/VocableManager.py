# -*- coding: utf-8 -*-
from AppSettings import AppSettings
from FileManager import FileManager
from exceptions.UnknownVocableException import UnknownVocableException

__author__ = 'xiaolong'


class VocableManager:

    vocables = []
    search_result = []

    def __init__(self):
        pass

    @classmethod
    def remove_vocable(cls, vocable):
        if vocable in VocableManager.vocables:
            VocableManager.vocables.remove(vocable)
            del vocable
        else:
            raise UnknownVocableException('Vocable not found.')

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
        xml_file_path = AppSettings.get_setting_by_name(AppSettings.XML_VOCABLE_FILE_PATH_SETTING_NAME)
        xsd_file_path = AppSettings.get_setting_by_name(AppSettings.XSD_VOCABLE_FILE_PATH_SETTING_NAME)

        VocableManager.vocables = FileManager.load_vocables(xml_file_path, xsd_file_path)
        VocableManager.search_result = VocableManager.vocables

    @classmethod
    def save_vocables(cls, vocable_list):
        xml_file_path = AppSettings.get_setting_by_name(AppSettings.XML_VOCABLE_FILE_PATH_SETTING_NAME)
        xsd_file_path = AppSettings.get_setting_by_name(AppSettings.XSD_VOCABLE_FILE_PATH_SETTING_NAME)
        FileManager.save_vocables(vocable_list, xml_file_path, xsd_file_path)
