import pytest as pytest
from xmltools.xmlparser import XMLParser

__author__ = 'xiaolong'


class TestTemplate:
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
            xsd_filename='/home/xiaolong/development/pycharm-workspace/gtkplus-tool/res/xld-vocables-schema-test.xsd',
            xml_filename='/home/xiaolong/development/pycharm-workspace/gtkplus-tool/res/vocables.xml'
        ), 'Your XML file is not valid against the provided XSD file.'
