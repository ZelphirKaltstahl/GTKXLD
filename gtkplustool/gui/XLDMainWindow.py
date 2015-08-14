# -*- coding: utf-8 -*-
from gi.repository import Gtk

__author__ = 'xiaolong'


class XLDMainWindow(Gtk.Window):
    def __init__(self):
        #super().__init__(title='Xiaolong Dictionary')
        super(XLDMainWindow, self).__init__(title='Xiaolong Dictionary')

        self.initialize_widgets()
        self.add_widgets()

    def initialize_widgets(self):
        pass

    def add_widgets(self):
        pass

