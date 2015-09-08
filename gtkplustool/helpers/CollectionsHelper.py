# -*- coding: utf-8 -*-
__author__ = 'xiaolong'


class CollectionsHelper:
    def __init__(self):
        pass

    @classmethod
    def all_unique(cls, collection):
        seen_items = set()
        return not any(i in seen_items or seen_items.add(i) for i in collection)
