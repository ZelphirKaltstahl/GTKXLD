# -*- coding: utf-8 -*-
from Settings import SETTINGS
import Settings
from model.Vocable import Vocable
from xmltools.xmlparser import XMLParser

__author__ = 'xiaolong'


class FileManager():
    def __init__(self):
        pass

    FIRST_LANGUAGE_TRANSLATIONS_ATTRIBUTE_NAME = 'firstLanguageTranslations'
    FIRST_LANGUAGE_PHONETIC_SCRIPT_ATTRIBUTE_NAME = 'firstLanguagePhoneticScripts'
    SECOND_LANGUAGE_TRANSLATIONS_ATTRIBUTE_NAME = 'secondLanguageTranslations'
    SECOND_LANGUAGE_PHONETIC_SCRIPT_ATTRIBUTE_NAME = 'secondLanguagePhoneticScripts'
    TOPICS_ATTRIBUTE_NAME = 'topics'
    CHAPTERS_ATTRIBUTE_NAME = 'chapters'
    LEARN_LEVEL_ATTRIBUTE_NAME = 'learnLevel'
    RELEVANCE_LEVEL_ATTRIBUTE_NAME = 'relevanceLevel'
    DESCRIPTION_ATTRIBUTE_NAME = 'description'

    @classmethod
    def load_vocables(cls):
        xml_path = SETTINGS[Settings.XML_VOCABLE_FILE_PATH]
        xsd_path = SETTINGS[Settings.XSD_FILE_PATH]

        vocables = []
        xmlparser = XMLParser()
        xml_root = xmlparser.get_xml_element_tree_root(xsd_filename=xsd_path, xml_filename=xml_path)

        for item in xml_root:
            vocable = Vocable(
                first_language_translations=item.find(FileManager.FIRST_LANGUAGE_TRANSLATIONS_ATTRIBUTE_NAME).text,
                first_language_phonetic_scripts=item.find(FileManager.FIRST_LANGUAGE_PHONETIC_SCRIPT_ATTRIBUTE_NAME).text,
                second_language_translations=item.find(FileManager.SECOND_LANGUAGE_TRANSLATIONS_ATTRIBUTE_NAME).text,
                second_language_phonetic_scripts=item.find(FileManager.SECOND_LANGUAGE_PHONETIC_SCRIPT_ATTRIBUTE_NAME).text,
                topics=item.find(FileManager.TOPICS_ATTRIBUTE_NAME).text,
                chapters=item.find(FileManager.CHAPTERS_ATTRIBUTE_NAME).text,
                learn_level=item.find(FileManager.LEARN_LEVEL_ATTRIBUTE_NAME).text,
                relevance_level=item.find(FileManager.RELEVANCE_LEVEL_ATTRIBUTE_NAME).text,
                description=item.find(FileManager.DESCRIPTION_ATTRIBUTE_NAME).text,
            )
            vocables.append(vocable)

        return vocables