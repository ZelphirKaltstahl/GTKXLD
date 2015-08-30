# -*- coding: utf-8 -*-
from filetools.path_helper import get_full_path

__author__ = 'xiaolong'

XML_VOCABLE_FILE_PATH = 'xml_vocable_file_path'
XSD_FILE_PATH = 'xsd_file_path'

SETTINGS = {
    XML_VOCABLE_FILE_PATH: get_full_path('res/vocables', 'vocables.xml'),
    XSD_FILE_PATH: get_full_path('res/vocables', 'xld-vocables-schema.xsd')
}
