# -*- coding: utf-8 -*-
from gi.repository import Gtk

__author__ = 'xiaolong'


class TrainingPage(Gtk.Grid):
    def __init__(self):
        super().__init__()

        self.set_hexpand(True)
        self.set_vexpand(True)
        self.set_row_spacing(4)
        self.set_column_spacing(4)

        self.initialize_widgets()
        self.add_widgets()

    def initialize_widgets(self):
        pass

    def add_widgets(self):
        pass
