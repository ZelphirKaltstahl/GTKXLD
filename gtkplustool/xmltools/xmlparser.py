# -*- coding: utf-8 -*-
from xmltools.XMLParseException import XMLParserException

__author__ = 'xiaolong'

import re
from xml.dom import minidom

from lxml import etree

__author__ = 'xiaolong'


class XMLParser:
    """
    This class is a XML parser which can validate ml files against a xml schema definition.
    """

    def __init__(self):
        pass

    @classmethod
    def validate_file(cls, xsd_filename="log_schema.xsd", xml_filename="log.xml"):
        print('validating XML file ...')

        # create a schema document by parsing the content of the xsd file
        xml_schema_document = etree.parse(xsd_filename)

        # create a schema using the schema document
        xmlschema = etree.XMLSchema(xml_schema_document)

        # create a xml document by parsing the content of the xml file
        xml_document = etree.parse(xml_filename)

        # try to validate the file
        return xmlschema.validate(xml_document)

    @classmethod
    def validate_tree(cls, xsd_filename, xml_tree):
        print('validating xml tree ...')
        # create a schema document by parsing the content of the xsd file
        xml_schema_document = etree.parse(xsd_filename)
        # create a schema using the schema document
        xmlschema = etree.XMLSchema(xml_schema_document)

        return xmlschema.validate(xml_tree)

    @classmethod
    def get_xml_element_tree_root(cls, xsd_filename="log_schema.xsd", xml_filename="log.xml"):
        if XMLParser.validate_file(xsd_filename=xsd_filename, xml_filename=xml_filename):
            with open(xml_filename, 'r') as f:
                file_content = f.read()

                if file_content.startswith("<?"):
                    file_content = re.sub("^\<\?.*?\?\>", '', file_content, flags=re.DOTALL)

                return etree.XML(file_content)
        else:
            raise XMLParserException("XML file invalid!")

    @classmethod
    def write_xml_file(
            cls,
            file,
            xml_root_element,
            xml_declaration=False
    ):
        rough_string = etree.tostring(xml_root_element, encoding='unicode', xml_declaration=xml_declaration)
        reparsed = minidom.parseString(rough_string)
        pretty_printed = reparsed.toprettyxml(indent='\t', encoding='utf-8')

        file.write(pretty_printed)
