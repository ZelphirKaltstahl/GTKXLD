# -*- coding: utf-8 -*-
__author__ = 'xiaolong'


class SearchFilter:
    """" This class shall be used as follows:
    - A search is done
    - for each attribute, used or not used in the search, a filter will be added to a list of used filters
        - for each unused attribute, the filter will always delegate vocables to the next filter
        - for each used attribute, the filter will check if the conditions specified by the user are met by the vocable and then either delegate the vocable or not
    - for an AND search, filters will be added to the end of the list of filters
    - for an OR search, filters will be added as a parallel filter path to the origin
    - every node carries a reference for the next filter
    - if next is None, it'll return true or false instead of delegating the choice to the next filter
    - the origin will wait for all branches to return and then decide if a vocable is in a search result or not
    - for each attribute of a vocable, there is one filter class extending this ABC
    """
    next = None

    def __init__(self):
        pass
