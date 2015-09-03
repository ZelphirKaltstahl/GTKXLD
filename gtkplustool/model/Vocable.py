# -*- coding: utf-8 -*-
from AppSettings import AppSettings

__author__ = 'xiaolong'


class Vocable:

    delimiter = None

    def __init__(
        self,
        first_language_translations=[],
        first_language_phonetic_scripts=[],
        second_language_translations=[],
        second_language_phonetic_scripts=[],
        topics=[],
        chapters=[],
        learn_level='0',
        relevance_level='0',
        description='---'
    ):
        self.first_language_translations = first_language_translations
        self.first_language_phonetic_scripts = first_language_phonetic_scripts
        self.second_language_translations = second_language_translations
        self.second_language_phonetic_scripts = second_language_phonetic_scripts
        self.topics = topics
        self.chapters = chapters
        self.learn_level = learn_level
        self.relevance_level = relevance_level
        self.description = description

        Vocable.delimiter = AppSettings.get_setting_by_name(AppSettings.ATTRIBUTE_VALUE_SEPARATOR_SETTING_NAME)

    def __str__(self):
        return '<Vocable> with ' + \
               Vocable.delimiter.join(self.first_language_translations) + ', ' + \
               Vocable.delimiter.join(self.first_language_phonetic_scripts) + ', ' + \
               Vocable.delimiter.join(self.second_language_translations) + ', ' + \
               Vocable.delimiter.join(self.second_language_phonetic_scripts) + ', ' + \
               Vocable.delimiter.join(self.topics) + ', ' + \
               Vocable.delimiter.join(self.chapters) + ', ' + \
               self.learn_level + ', ' + \
               self.relevance_level + ', ' + \
               self.description
