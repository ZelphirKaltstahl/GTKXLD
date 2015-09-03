# -*- coding: utf-8 -*-
from lxml import etree
from filetools.path_helper import get_full_path
from xmltools.XMLInvalidException import XMLInvalidException
from xmltools.xmlparser import XMLParser

__author__ = 'xiaolong'

from exceptions.SettingUnknownException import SettingUnknownException


class AppSettings:
    settings = None
    xml_root = None

    XML_VOCABLE_FILE_PATH_SETTING_NAME = 'xml_vocable_file_path'
    XSD_VOCABLE_FILE_PATH_SETTING_NAME = 'xsd_vocable_file_path'

    ATTRIBUTE_VALUE_SEPARATOR_SETTING_NAME = 'attribute_value_separator'
    STRIPPED_CHARACTERS_SETTING_NAME = 'stripped_characters'

    INITIAL_TREEVIEW_COLUMN_WIDTH = 'initial_treeview_column_width'

    SAVE_VOCABLES_ON_EXIT_SETTING_NAME = 'save_vocables_on_exit'
    DIALOG_SHOW_SAVE_VOCABLES_CONFIRMATION_SETTING_NAME = 'dialog_show_save_vocables_confirmation'
    DIALOG_SHOW_EXIT_CONFIRMATION_SETTING_NAME = 'dialog_show_exit_confirmation'

    def __init__(self):
        pass

    @classmethod
    def get_setting_by_name(cls, name):
        if name in AppSettings.settings:
            return AppSettings.settings[name]
        else:
            raise SettingUnknownException('Tried to access a setting, which is not available or unkown.')

    @classmethod
    def set_setting_by_name(cls, name, value):
        print('Changing setting:', name, ' VALUE:', value)
        if name in AppSettings.settings:
            AppSettings.settings[name] = str(value)
        else:
            raise SettingUnknownException('Tried to access a setting, which is not available or unkown.')

    @classmethod
    def load_settings(cls):
        xml_settings_file_path = get_full_path('res/settings', 'settings.xml')
        xsd_settings_file_path = get_full_path('res/settings', 'settings.xsd')

        AppSettings.settings = {}
        xmlparser = XMLParser()
        AppSettings.xml_root = xmlparser.get_xml_element_tree_root(xsd_settings_file_path, xml_settings_file_path)

        for item in AppSettings.xml_root:
            AppSettings.settings[item.find('name').text] = item.find('value').text

        for key, value in AppSettings.settings.items():
            print('Key:', key)
            print('Value:', value)

    @classmethod
    def save_settings(cls):
        print('trying to save settings:', AppSettings.settings)

        xml_settings_file_path = get_full_path('res/settings', 'settings.xml')
        xsd_settings_file_path = get_full_path('res/settings', 'settings.xsd')

        xml_parser = XMLParser()

        new_xml_root = etree.Element('list')
        for key, value in AppSettings.settings.items():
            setting_node = etree.SubElement(new_xml_root, 'setting')
            name_node = etree.SubElement(setting_node, 'name')
            name_node.text = key
            value_node = etree.SubElement(setting_node, 'value')
            value_node.text = value

        if xml_parser.validate_tree(xsd_settings_file_path, new_xml_root):
            xml_parser.write_xml_file(xml_settings_file_path, new_xml_root)
        else:
            raise XMLInvalidException('The XML is not valid.')

    @classmethod
    def append_setting(cls, key, value):
        pass
