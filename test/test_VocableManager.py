from random import randint
import pytest as pytest
from AppSettings import AppSettings
from VocableManager import VocableManager

__author__ = 'xiaolong'


def all_unique(x):
    seen = set()
    return not any(i in seen or seen.add(i) for i in x)

# TODO: remove_vocable_by_index
# TODO: add_vocable
# TODO: set_search_result
# TODO: get_search_result
# TODO: get_search_result_vocable
# TODO: load_vocables
# TODO: save_vocables(cls, vocable_list):


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

    @pytest.fixture()
    def load_vocables(self):
        AppSettings.load_settings()
        VocableManager.load_vocables()

    @pytest.mark.usefixtures('load_vocables')
    def test_xml_file_invariance(self):
        # get file content
        xml_file_content = None
        xml_file_path = AppSettings.get_setting_by_name(AppSettings.XML_VOCABLE_FILE_PATH_SETTING_NAME)
        with open(xml_file_path, mode='rb') as vocable_file:
            xml_file_content = vocable_file.read()

        # get vocables
        vocables = VocableManager.vocables

        # save vocables
        VocableManager.save_vocables(vocables)

        # check if file content is still the same
        new_xml_file_content = None
        xml_file_path = AppSettings.get_setting_by_name(AppSettings.XML_VOCABLE_FILE_PATH_SETTING_NAME)
        with open(xml_file_path, mode='rb') as vocable_file:
            new_xml_file_content = vocable_file.read()

        assert xml_file_content == new_xml_file_content, \
            'Loading and saving the vocables leads to changes in the XML vocable file, ' \
            'although the vocables didn\'t change. These changes might be whitespace character differences.'

        # check if the vocables are still the same
        VocableManager.load_vocables()
        new_vocables = VocableManager.vocables

        # test object inequality
        assert vocables[0] != new_vocables[0], \
            'The compared vocable objects are identical.'

        # for all vocables
        for index in range(len(vocables)):

            # for all first language translations
            for attribute_index in range(len(vocables[index].first_language_translations)):
                first_language_transaltion_1 = vocables[index].first_language_translations[attribute_index]
                first_language_transaltion_2 = new_vocables[index].first_language_translations[attribute_index]

                assert first_language_transaltion_1 == first_language_transaltion_2, \
                    'There are differences in a vocable\'s first_language_translations attribute.'

            # for all first language phonetic scripts
            for attribute_index in range(len(vocables[index].first_language_phonetic_scripts)):
                first_language_phonetic_script_1 = vocables[index].first_language_phonetic_scripts[attribute_index]
                first_language_phonetic_script_2 = new_vocables[index].first_language_phonetic_scripts[attribute_index]

                assert first_language_phonetic_script_1 == first_language_phonetic_script_2, \
                    'There are differences in a vocable\'s first_language_phonetic_scripts attribute.'

            # for all second language translations
            for attribute_index in range(len(vocables[index].second_language_translations)):
                second_language_transaltion_1 = vocables[index].second_language_translations[attribute_index]
                second_language_transaltion_2 = new_vocables[index].second_language_translations[attribute_index]

                assert second_language_transaltion_1 == second_language_transaltion_2, \
                    'There are differences in a vocable\'s second_language_translations attribute.'

            # for all second language phonetic scripts
            for attribute_index in range(len(vocables[index].second_language_phonetic_scripts)):
                second_language_phonetic_script_1 = vocables[index].second_language_phonetic_scripts[attribute_index]
                second_language_phonetic_script_2 = new_vocables[index].second_language_phonetic_scripts[attribute_index]

                assert second_language_phonetic_script_1 == second_language_phonetic_script_2, \
                    'There are differences in a vocable\'s second_language_phonetic_scripts attribute.'

            # for all topics scripts
            for attribute_index in range(len(vocables[index].topics)):
                topic_1 = vocables[index].topics[attribute_index]
                topic_2 = new_vocables[index].topics[attribute_index]

                assert topic_1 == topic_2, \
                    'There are differences in a vocable\'s topics attribute.'

            # for all chapters scripts
            for attribute_index in range(len(vocables[index].chapters)):
                chapter_1 = vocables[index].chapters[attribute_index]
                chapter_2 = new_vocables[index].chapters[attribute_index]

                assert chapter_1 == chapter_2, \
                    'There are differences in a vocable\'s chapters attribute.'

            assert vocables[index].learn_level == new_vocables[index].learn_level, \
                'There are differences in a vocable\'s learn_level attribute.'

            assert vocables[index].relevance_level == new_vocables[index].relevance_level, \
                'There are differences in a vocable\'s relevance_level attribute.'

            assert vocables[index].description == new_vocables[index].description, \
                'There are differences in a vocable\'s description attribute.'

    @pytest.mark.usefixtures('load_vocables')
    def test_remove_vocable(self):
        number_of_vocables = len(VocableManager.vocables)
        random_indices = []
        selected_vocables = []
        for index in range(100):
            # get an index, which we've not yet selected
            random_index = randint(0, number_of_vocables-1)
            while random_index in random_indices:
                random_index = randint(0, number_of_vocables-1)
            random_indices.append(random_index)
            selected_vocables.append(VocableManager.vocables[random_index])

        assert all_unique(random_indices), 'Trying to remove vocable of one and the same index twice during test.'

        for selected_vocable in selected_vocables:
            VocableManager.remove_vocable(selected_vocable)
            assert selected_vocable not in VocableManager.vocables, 'Vocable was not deleted from vocables.'

        for selected_vocable in selected_vocables:
            assert selected_vocable not in VocableManager.vocables, 'Vocable was not deleted from vocables.'

    @pytest.mark.usefixtures('load_vocables')
    def test_remove_vocable_throws_exception(self):
        # TODO: throws only when vocable not in list, but then does throw UnknownVocableException
        pass