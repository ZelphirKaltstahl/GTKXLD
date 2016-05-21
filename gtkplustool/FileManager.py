# -*- coding: utf-8 -*-
from xml.dom import minidom
from lxml import etree
from xmltools.XMLEtreeHelper import XMLEtreeHelper
from xmltools.XMLInvalidException import XMLInvalidException

__author__ = 'xiaolong'

from AppSettings import AppSettings
from model.Vocable import Vocable
from xmltools.XMLParser import XMLParser


class FileManager:
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
    def load_vocables(cls, xml_file_path, xsd_file_path):
        vocables = []
        xmlparser = XMLParser()
        xml_root = xmlparser.get_xml_element_tree_root(xsd_file_path, xml_file_path)

        for item in xml_root:
            vocable = Vocable(
                first_language_translations=FileManager.get_attribute_value_list_from_string(
                    item.find(FileManager.FIRST_LANGUAGE_TRANSLATIONS_ATTRIBUTE_NAME).text
                ),
                first_language_phonetic_scripts=FileManager.get_attribute_value_list_from_string(
                    item.find(FileManager.FIRST_LANGUAGE_PHONETIC_SCRIPT_ATTRIBUTE_NAME).text
                ),
                second_language_translations=FileManager.get_attribute_value_list_from_string(
                    item.find(FileManager.SECOND_LANGUAGE_TRANSLATIONS_ATTRIBUTE_NAME).text
                ),
                second_language_phonetic_scripts=FileManager.get_attribute_value_list_from_string(
                    item.find(FileManager.SECOND_LANGUAGE_PHONETIC_SCRIPT_ATTRIBUTE_NAME).text
                ),
                topics=FileManager.get_attribute_value_list_from_string(
                    item.find(FileManager.TOPICS_ATTRIBUTE_NAME).text
                ),
                chapters=FileManager.get_attribute_value_list_from_string(
                    item.find(FileManager.CHAPTERS_ATTRIBUTE_NAME).text
                ),
                learn_level=item.find(FileManager.LEARN_LEVEL_ATTRIBUTE_NAME).text,
                relevance_level=item.find(FileManager.RELEVANCE_LEVEL_ATTRIBUTE_NAME).text,
                description=item.find(FileManager.DESCRIPTION_ATTRIBUTE_NAME).text,
            )
            vocables.append(vocable)

        return vocables

    @classmethod
    def get_attribute_value_list_from_string(cls, string):
        attribute_value_separator = AppSettings.get_setting_by_name(AppSettings.ATTRIBUTE_VALUE_SEPARATOR_SETTING_NAME)
        stripped_characters = AppSettings.get_setting_by_name(AppSettings.STRIPPED_CHARACTERS_SETTING_NAME)

        value_list = string.split(sep=attribute_value_separator, maxsplit=-1)
        # stripped_value_list = [value.strip(stripped_characters) for value in value_list]

        # return stripped_value_list
        return value_list

    @classmethod
    def save_vocables(cls, vocable_list, xml_file_path, xsd_file_path):
        delimiter = AppSettings.get_setting_by_name(AppSettings.ATTRIBUTE_VALUE_SEPARATOR_SETTING_NAME)
        xml_parser = XMLParser()

        new_xml_root = etree.Element('list')
        for vocable in vocable_list:
            vocable_node = FileManager.create_vocable_xml_node(new_xml_root, vocable, delimiter)

        # # test print
        # rough_string = etree.tostring(new_xml_root, encoding='unicode')
        # reparsed = minidom.parseString(rough_string)
        # pretty_printed = reparsed.toprettyxml(indent='\t', encoding='utf-8')
        # print(pretty_printed[:600])
        # with open('/home/xiaolong/testfile.xml', 'w') as file:
        #     file.write(str(pretty_printed))
        # # end

        if xml_parser.validate_tree(xsd_file_path, new_xml_root):
            xml_parser.write_xml_file(xml_file_path, new_xml_root)
        else:
            raise XMLInvalidException(
                'The XML is not valid. Could not write vocables to file: ' +
                xml_file_path +
                ' validating against XSD: '
                + xsd_file_path
            )

    @classmethod
    def create_vocable_xml_node(cls, parent_node, vocable, delimiter):
        vocable_node = etree.SubElement(parent_node, 'vocable')

        first_language_translations_xml_node = XMLEtreeHelper.create_node(
            vocable_node,
            FileManager.FIRST_LANGUAGE_TRANSLATIONS_ATTRIBUTE_NAME,
            delimiter.join(vocable.first_language_translations)
        )
        first_language_phonetic_scripts_xml_node = XMLEtreeHelper.create_node(
            vocable_node,
            FileManager.FIRST_LANGUAGE_PHONETIC_SCRIPT_ATTRIBUTE_NAME,
            delimiter.join(vocable.first_language_phonetic_scripts)
        )
        second_language_translations_xml_node = XMLEtreeHelper.create_node(
            vocable_node,
            FileManager.SECOND_LANGUAGE_TRANSLATIONS_ATTRIBUTE_NAME,
            delimiter.join(vocable.second_language_translations)
        )
        second_language_phonetic_scripts_xml_node = XMLEtreeHelper.create_node(
            vocable_node,
            FileManager.SECOND_LANGUAGE_PHONETIC_SCRIPT_ATTRIBUTE_NAME,
            delimiter.join(vocable.second_language_phonetic_scripts)
        )

        topics_xml_node = XMLEtreeHelper.create_node(
            vocable_node,
            FileManager.TOPICS_ATTRIBUTE_NAME,
            delimiter.join(vocable.topics)
        )
        chapters_xml_node = XMLEtreeHelper.create_node(
            vocable_node,
            FileManager.CHAPTERS_ATTRIBUTE_NAME,
            delimiter.join(vocable.chapters)
        )

        description_xml_node = XMLEtreeHelper.create_node(
            vocable_node,
            FileManager.DESCRIPTION_ATTRIBUTE_NAME,
            vocable.description
        )

        learn_level_xml_node = XMLEtreeHelper.create_node(
            vocable_node,
            FileManager.LEARN_LEVEL_ATTRIBUTE_NAME,
            vocable.learn_level
        )
        relevance_level_xml_node = XMLEtreeHelper.create_node(
            vocable_node,
            FileManager.RELEVANCE_LEVEL_ATTRIBUTE_NAME,
            vocable.relevance_level
        )

        return vocable_node