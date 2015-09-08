import pytest as pytest
from helpers.CollectionsHelper import CollectionsHelper

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

    def test_all_unique(self):
        # works with length 5
        assert CollectionsHelper.all_unique(['a', 'b', 'c', 'd','e']), \
            'The method CollectionsHelper.all_unique does not work correctly.'

        # works with a different length (4)
        assert CollectionsHelper.all_unique(['a', 'b', 'c', 'd']), \
            'The method CollectionsHelper.all_unique does not work correctly.'

        # works if there are duplicate 'a' next to each other
        assert not CollectionsHelper.all_unique(['a', 'a', 'c', 'd','e']), \
            'The method CollectionsHelper.all_unique does not work correctly.'

        # works if the duplicate items are not next to each other
        assert not CollectionsHelper.all_unique(['a', 'b', 'a', 'd','e']), \
            'The method CollectionsHelper.all_unique does not work correctly.'

        # works for other characters than 'a'
        assert not CollectionsHelper.all_unique(['a', 'b', 'c', 'b','e']), \
            'The method CollectionsHelper.all_unique does not work correctly.'

        # lower case upper case distinguishing
        assert CollectionsHelper.all_unique(['a', 'A', 'c', 'd','e']), \
            'The method CollectionsHelper.all_unique does not work correctly.'

        # works for numbers as well
        assert CollectionsHelper.all_unique([1, 2, 3, 4]), \
            'The method CollectionsHelper.all_unique does not work correctly.'
        assert CollectionsHelper.all_unique([1, 2, 3, 4, 5]), \
            'The method CollectionsHelper.all_unique does not work correctly.'
        assert not CollectionsHelper.all_unique([1, 2, 2, 4, 5]), \
            'The method CollectionsHelper.all_unique does not work correctly.'
        assert not CollectionsHelper.all_unique([1, 2, 5, 4, 5]), \
            'The method CollectionsHelper.all_unique does not work correctly.'