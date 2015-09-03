# -*- coding: utf-8 -*-
from gi.repository import Gtk
from math import log10
from AppSettings import AppSettings
from VocableManager import VocableManager
from gui.BigCharacterBox import BigCharacterBox
from gui.XLDVocableTreeView import XLDVocableTreeView
from helpers.StringHelper import len_of_number, zero_fill

__author__ = 'xiaolong'


class XLDDictionaryPage(Gtk.Grid):
    sortable_vocable_tree_view_model = None
    xld_vocabletreeview = None
    scrolled_window = None
    scrolled_window_frame = None
    big_character_box = None

    def __init__(self):
        super().__init__()

        self.set_hexpand(True)
        self.set_vexpand(True)
        self.set_row_spacing(4)
        self.set_column_spacing(4)

        self.initialize_widgets()
        self.add_widgets()

    def initialize_widgets(self):
        self.sortable_vocable_tree_view_model = self.create_sortable_vocable_tree_view_model()
        self.xld_vocabletreeview = XLDVocableTreeView()
        self.xld_vocabletreeview.set_model(self.sortable_vocable_tree_view_model)

        self.scrolled_window_frame = Gtk.Frame()
        self.scrolled_window_frame.set_name('vocable_treeview_scrolled_window_frame')

        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.set_policy(
            hscrollbar_policy=Gtk.PolicyType.AUTOMATIC,
            vscrollbar_policy=Gtk.PolicyType.AUTOMATIC
        )
        self.scrolled_window.set_hexpand(True)
        self.scrolled_window.set_vexpand(True)

        self.big_character_box = BigCharacterBox()
        self.big_character_box.set_name('big_character_box')

    def add_widgets(self):
        self.scrolled_window.add(self.xld_vocabletreeview)
        self.scrolled_window_frame.add(self.scrolled_window)
        self.attach(child=self.scrolled_window_frame, left=0, top=0, width=1, height=1)
        self.attach(child=self.big_character_box, left=1, top=0, width=1, height=1)

    def create_sortable_vocable_tree_view_model(self):
        vocable_tree_view_model = Gtk.ListStore(str, str, str, str, str)  # index, fl, flps, slps, sl
        displayed_vocable_attributes_list = []

        delimiter = AppSettings.get_setting_by_name(AppSettings.ATTRIBUTE_VALUE_SEPARATOR_SETTING_NAME)

        for vocable in VocableManager.search_result:
            displayed_vocable_attributes_list.append(
                (
                    delimiter.join(vocable.first_language_translations),
                    delimiter.join(vocable.first_language_phonetic_scripts),
                    delimiter.join(vocable.second_language_phonetic_scripts),
                    delimiter.join(vocable.second_language_translations)
                )
            )

        for list_index, vocable in enumerate(displayed_vocable_attributes_list):
            string_index = zero_fill(str(list_index), len_of_number(len(displayed_vocable_attributes_list)))
            row = [string_index]
            for attribute in vocable:
                row.append(attribute)
            vocable_tree_view_model.append(row)
            # vocable_tree_view_model.append(Vocable('fl','flps','sl','slps','t','c','ll','rl','d')) # This does not work because of number of columns issue

        # make it sortable
        sortable_vocable_tree_view_model = Gtk.TreeModelSort(model=vocable_tree_view_model)

        return sortable_vocable_tree_view_model