import random
import string
import pytest as pytest
from AppSettings import AppSettings
from exceptions.SettingUnknownException import SettingUnknownException
from filetools.path_helper import get_full_path

__author__ = 'xiaolong'


class TestAppSettings:
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

    def randomword(self, length):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

    @pytest.fixture()
    def load_settings(self):
        AppSettings.load_settings()

    def test_xml_settings_file_invariance(self):
        xml_settings_file_path = get_full_path('res/settings', 'settings.xml')

        settings_file_content_1 = None
        with open(xml_settings_file_path, 'rb') as settings_file:
            settings_file_content_1 = settings_file.read()

        AppSettings.load_settings()
        settings_1 = AppSettings.settings

        AppSettings.save_settings()

        settings_file_content_2 = None
        with open(xml_settings_file_path, 'rb') as settings_file:
            settings_file_content_2 = settings_file.read()

        AppSettings.load_settings()
        settings_2 = AppSettings.settings

        # equality does not work, since dictionaries do not have an invariant order of access,
        # but something weaker might work

        # assert settings_file_content_1 == settings_file_content_2, \
        #     'Loading and saving the settings causes changes in the XML settings file, ' \
        #     'although the settings didn\'t change. These changes might be whitespace character differences.'

        assert len(settings_file_content_1) == len(settings_file_content_2), \
            'The settings file contents differ in length.'

        for character in settings_file_content_1:
            assert character in settings_file_content_2, \
                'There is content in one settings file, which is not in the other.'

        for character in settings_file_content_2:
            assert character in settings_file_content_1, \
                'There is content in one settings file, which is not in the other.'

        characters_1 = {}
        for character in settings_file_content_1:
            if character in characters_1:
                characters_1[character] += 1
            else:
                characters_1[character] = 1

        characters_2 = {}
        for character in settings_file_content_2:
            if character in characters_2:
                characters_2[character] += 1
            else:
                characters_2[character] = 1

        assert characters_1 == characters_2, \
            'The settings files do not contain the same characters.'

        assert settings_1 == settings_2, \
            'Loading and saving the settings causes changes in the settings, ' \
            'although were not intentionally changed.'

    @pytest.mark.usefixtures('load_settings')
    def test_get_setting_by_name(self):
        """
        To test the get_setting_by_name method, we have to assert the following:
        1. trying to access a setting, which does not exist raises the appropriate exception
        2. trying to access a setting, which does exist, will return the correct settings value
        To assert 2., we can set a settings value using the change_setting_by_name or add_setting_by_name.
        """

        # make sure we have a string, which is not a key in the dictionary
        random_word_length = 10
        random_word = self.randomword(random_word_length)
        while random_word in AppSettings.settings:
            random_word_length += 1
            random_word = self.randomword(random_word_length)

        # check for 1. (does it throw the correct exception?)
        try:
            AppSettings.get_setting_by_name(random_word)
            assert False, 'Could get a value for a not existing setting.'
        except SettingUnknownException:
            assert random_word not in AppSettings.settings, \
                'The method AppSettings.get_setting_by_name falsely throws exception SettingUnknownException.'

        # check for 2.
        if len(AppSettings.settings.keys()) == 0:
            test_setting_name = 'test_setting_name'
            test_setting_value = 'test_setting_value'
            AppSettings.add_setting_by_name(test_setting_name, test_setting_value)
            assert AppSettings.get_setting_by_name(test_setting_name) == test_setting_value, \
                'The method AppSettings.get_setting_by_name does not return the correct value.'
        else:
            existing_dictionary_key = list(AppSettings.settings.keys())[0]
            try:
                returned_value = AppSettings.get_setting_by_name(existing_dictionary_key)
                expected_value = AppSettings.settings[existing_dictionary_key]
                assert returned_value == expected_value, \
                    'The method AppSettings.get_setting_by_name does not return the correct value.'
            except SettingUnknownException:
                assert False, 'Exception raised although the accessed key existed in the settings dictionary.'

    @pytest.mark.usefixtures('load_settings')
    def test_change_setting_by_name(self):
        """
        To test the method AppSettings.change_setting_by_name, we have to assert the following:
        1.Trying to change a setting, which does not exist should throw a SettingUnknownException.
        2.Trying to change a setting, which does exist, should result in the setting having the changed value.
        """
        # make sure we have a string, which is not a key in the dictionary
        random_word_length = 10
        random_word = self.randomword(random_word_length)
        while random_word in AppSettings.settings:
            random_word_length += 1
            random_word = self.randomword(random_word_length)

        # check for 1. (Does the method throw the correct exception?)
        try:
            AppSettings.change_setting_by_name(random_word, 'abc')
            assert False, 'Could change a not existing setting.'
        except SettingUnknownException:
            assert random_word not in AppSettings.settings, \
                'The method AppSettings.change_setting_by_name falsely throws exception SettingUnknownException.'

        # check for 2. (Does the method set the correct value for the setting?)
        if len(AppSettings.settings.keys()) == 0:
            test_setting_name = 'test_setting_name'
            test_setting_value = 'test_setting_value'
            new_value = test_setting_value + '_1'
            AppSettings.add_setting_by_name(test_setting_name, test_setting_value)
            AppSettings.change_setting_by_name(test_setting_name, new_value)
            assert AppSettings.get_setting_by_name(test_setting_name) == new_value, \
                'The method AppSettings.change_setting_by_name not set the correct value.'
        else:
            existing_dictionary_key = list(AppSettings.settings.keys())[0]
            try:
                old_value = AppSettings.get_setting_by_name(existing_dictionary_key)
                new_value = old_value + '_1'
                AppSettings.change_setting_by_name(existing_dictionary_key, new_value)
                assert AppSettings.get_setting_by_name(existing_dictionary_key) == new_value, \
                    'The method AppSettings.change_setting_by_name does change to the correct value.'
            except SettingUnknownException:
                assert False, 'AppSettings.change_setting_by_name a SettingUnknownException, ' \
                              'although the accessed key existed in the settings dictionary.'
