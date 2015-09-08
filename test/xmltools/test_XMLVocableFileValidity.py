import pytest as pytest
from filetools.path_helper import get_full_path
from xmltools.XMLParser import XMLParser

__author__ = 'xiaolong'


class TestXMLVocableFileValidity:
    def setup(self):
        pass

    def teardown(self):
        pass

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_xml_file_validity(self):
        assert XMLParser.validate_file(
            xsd_file_path=get_full_path('res/vocables', 'vocables.xsd'),
            xml_file_path=get_full_path('res/vocables', 'vocables.xml'),
        ), 'Your XML vocables file is not valid against the provided XSD file.'
