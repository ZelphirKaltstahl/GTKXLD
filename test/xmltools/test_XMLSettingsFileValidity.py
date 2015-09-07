import pytest as pytest
from filetools.path_helper import get_full_path
from xmltools.xmlparser import XMLParser

__author__ = 'xiaolong'


class TestXMLSettingsFileValidity:
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
            xsd_file_path=get_full_path('res/settings', 'settings.xsd'),
            xml_file_path=get_full_path('res/settings', 'settings.xml'),
        ), 'Your XML settings file is not valid against the provided XSD file.'
