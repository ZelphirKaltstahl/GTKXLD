from random import *
import pytest as pytest
from AppSettings import AppSettings
from VocableManager import VocableManager
from helpers.RandomStringCreator import RandomStringCreator
from model.Vocable import Vocable

__author__ = 'xiaolong'


class TestVocable:
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

    def create_random_vocable(self):
        return Vocable(
            first_language_translations=[RandomStringCreator.randomword(10)],
            first_language_phonetic_scripts=[RandomStringCreator.randomword(10)],
            second_language_translations=[RandomStringCreator.randomword(10)],
            second_language_phonetic_scripts=[RandomStringCreator.randomword(10)],
            topics=[RandomStringCreator.randomword(10)],
            chapters=[RandomStringCreator.randomword(10)],
            learn_level=str(randint(0, 5)),
            relevance_level=str(randint(0, 5)),
            description=RandomStringCreator.randomword(10)
        )

    def copy_vocable(self, vocable):
        return Vocable(
            first_language_translations=vocable.first_language_translations,
            first_language_phonetic_scripts=vocable.first_language_phonetic_scripts,
            second_language_translations=vocable.second_language_translations,
            second_language_phonetic_scripts=vocable.second_language_phonetic_scripts,
            topics=vocable.topics,
            chapters=vocable.chapters,
            learn_level=vocable.learn_level,
            relevance_level=vocable.relevance_level,
            description=vocable.description
        )

    def partial_copy_vocable(self, vocable):
        return Vocable(
            first_language_translations=vocable.first_language_translations,
            first_language_phonetic_scripts=vocable.first_language_phonetic_scripts,
            second_language_translations=vocable.second_language_translations,
            second_language_phonetic_scripts=vocable.second_language_phonetic_scripts
        )

    def create_vocable_list(self):
        AppSettings.load_settings()

        list_of_vocables = []

        for index in range(10):
            vocable_not_in_list = self.create_random_vocable()

            while any(
                item for item in list_of_vocables
                if item.first_language_translations == vocable_not_in_list.first_language_translations
            ):
                vocable_not_in_list = self.create_random_vocable()

            list_of_vocables.append(vocable_not_in_list)

        return list_of_vocables

    def get_vocable_not_in_list(self, vocable_list):
        vocable_not_in_list = self.create_random_vocable()

        # only one attribute of the following attributes needs to be different, to make a different vocable:
        # - first language translations
        # - first language phonetic scripts
        # - second language translations
        # - second language phonetic scripts
        # In order to have a duplicate vocable, all of them need to be equal.
        while any(
            item for item in vocable_list
            if (
                item.first_language_translations == vocable_not_in_list.first_language_translations and
                item.first_language_phonetic_scripts == vocable_not_in_list.first_language_phonetic_scripts and
                item.second_language_translations == vocable_not_in_list.second_language_translations and
                item.second_language_phonetic_scripts == vocable_not_in_list.second_language_phonetic_scripts
            )
        ):
            vocable_not_in_list = self.create_random_vocable()

        return vocable_not_in_list

    @pytest.mark.unit
    def test_equals(self):
        vocable_list = self.create_vocable_list()
        vocable_not_in_list = self.get_vocable_not_in_list(vocable_list)

        assert isinstance(vocable_list, list), \
            'Variable create_vocable_list is not a list.'

        assert vocable_list[0] in vocable_list, \
            'The \'in\' operation does not work correctly'

        assert vocable_list[-1] in vocable_list, \
            'The \'in\' operation does not work correctly'

        for index, vocable in enumerate(vocable_list):
            # print('type of vocable:', type(vocable))
            # print('type of index:', type(index))
            #
            # print(self.copy_vocable(vocable))
            assert self.copy_vocable(vocable) == vocable_list[index], \
                'The copy of a Vocable does not equal the Vocable it was copied from.'

        for index, vocable in enumerate(vocable_list):
            assert self.partial_copy_vocable(vocable) == vocable_list[index], \
                'The partial copy of a Vocable does not equal the Vocable it was copied from.'

    @pytest.mark.unit
    def test_not_equals(self):
        vocable_list = self.create_vocable_list()
        vocable_not_in_list = self.get_vocable_not_in_list(vocable_list)

        assert isinstance(vocable_list, list), \
            'Variable create_vocable_list is not a list.'

        assert vocable_not_in_list not in vocable_list, \
            'The \'not in\' operation does not work correctly'

        changed_vocable = self.copy_vocable(vocable_list[0])
        changed_vocable.second_language_translations = \
            changed_vocable.second_language_translations.append('appended value')
        assert changed_vocable not in vocable_list, \
            'The \'not in\' operation does not work correctly'

        changed_vocable = self.copy_vocable(vocable_list[0])
        changed_second_language_translations = []
        for index, value in enumerate(changed_vocable.second_language_translations):
            if index == 0:
                changed_second_language_translations.append(value + '---')
            else:
                changed_second_language_translations.append(value)
        changed_vocable.second_language_translations = changed_second_language_translations
        assert changed_vocable not in vocable_list, \
            'The \'not in\' operation does not work correctly'
