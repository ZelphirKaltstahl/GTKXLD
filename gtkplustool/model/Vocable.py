# -*- coding: utf-8 -*-
__author__ = 'xiaolong'


class Vocable:
    def __init__(
        self,
        first_language_translations='---',
        first_language_phonetic_scripts='---',
        second_language_translations='---',
        second_language_phonetic_scripts='---',
        topics='---',
        chapters='---',
        learn_level='---',
        relevance_level='---',
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

    def __str__(self):
        return '<Vocable> with ' + \
               self.first_language_translations + ', ' + \
               self.first_language_phonetic_scripts + ', ' + \
               self.second_language_translations + ', ' + \
               self.second_language_phonetic_scripts + ', ' + \
               self.topics + ', ' + \
               self.chapters + ', ' + \
               self.learn_level + ', ' + \
               self.relevance_level + ', ' + \
               self.description