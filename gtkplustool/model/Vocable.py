# -*- coding: utf-8 -*-
from AppSettings import AppSettings
from decorators.overrides import overrides

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

    # def with_first_language_translations(self, translations):
    #     self.first_language_translations = translations
    #     return self
    #
    # def with_first_language_phonetic_scripts(self, phonetic_scripts):
    #     self.first_language_phonetic_scripts = phonetic_scripts
    #     return self
    #
    # def with_second_language_translations(self, translations):
    #     self.second_language_translations = translations
    #     return self
    #
    # def with_second_language_phonetic_scripts(self, phonetic_scripts):
    #     self.second_language_phonetic_scripts = phonetic_scripts
    #     return self
    #
    # def with_topics(self, topics):
    #     self.topics = topics
    #     return self
    #
    # def with_chapters(self, chapters):
    #     self.chapters = chapters
    #     return self
    #
    # def with_learn_level(self, level):
    #     self.learn_level = level
    #     return self
    #
    # def with_relevance_level(self, level):
    #     self.relevance_level = level
    #     return self
    #
    # def with_description(self, description):
    #     self.description = description
    #     return self

    @overrides(object)
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

    @overrides(object)
    def __eq__(self, other):
        """override the default equals behavior"""
        if isinstance(other, self.__class__):
            return \
                self.first_language_translations == other.first_language_translations and \
                self.first_language_phonetic_scripts == other.first_language_phonetic_scripts and \
                self.second_language_translations == other.second_language_translations and \
                self.second_language_phonetic_scripts == other.second_language_phonetic_scripts
        return NotImplemented

    @overrides(object)
    def __ne__(self, other):
        """define a non-equality test"""
        if isinstance(other, self.__class__):
            return \
                self.first_language_translations != other.first_language_translations or \
                self.first_language_phonetic_scripts != other.first_language_phonetic_scripts or \
                self.second_language_translations != other.second_language_translations or \
                self.second_language_phonetic_scripts != other.second_language_phonetic_scripts
        return NotImplemented

    @overrides(object)
    def __hash__(self):
        """override the default hash behavior (that returns the id or the object)"""
        return hash(
            tuple(
                self.first_language_translations,
                self.first_language_phonetic_scripts,
                self.second_language_translations,
                self.second_language_phonetic_scripts
            )
        )