# -*- coding: utf-8 -*-
from gi.repository import Gtk

__author__ = 'xiaolong'


class BigCharacterBox(Gtk.Grid):
    characters_label = None
    big_character_label = None
    previous_button = None
    next_button = None

    def __init__(self):
        super().__init__()

        self.add_widgets()

    def add_widgets(self):
        self.characters_label = Gtk.Label('Characters')
        self.big_character_label = Gtk.Label('中')
        self.previous_button = Gtk.Button('<<')
        self.next_button = Gtk.Button('<<')
