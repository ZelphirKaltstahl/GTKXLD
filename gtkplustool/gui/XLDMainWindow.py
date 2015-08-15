# -*- coding: utf-8 -*-
from gi.repository import Gtk
from gui.XLDMenuBar import XLDMenuBar

__author__ = 'xiaolong'


class XLDMainWindow(Gtk.Window):

    WINDOW_TITLE = 'Xiaolong Dictionary'
    DEFAULT_X_SIZE = 400
    DEFAULT_Y_SIZE = 300
    menubar = None

    def __init__(self):
        # super().__init__(title='Xiaolong Dictionary')
        super(XLDMainWindow, self).__init__(title=self.WINDOW_TITLE)

        self.set_default_size(self.DEFAULT_X_SIZE, self.DEFAULT_Y_SIZE)

        self.initialize_widgets()
        self.add_widgets()

    def initialize_widgets(self):
        self.menubar = XLDMenuBar(self)

    def add_widgets(self):
        self.add(self.menubar)

    def connect_signals(self):
        pass

    def create_ui_manager(self):
        uimanager = Gtk.UIManager()

        # Throws exception if something went wrong
        uimanager.add_ui_from_string(XLDMenuBar.MENUBAR_UI_INFO)

        # Add the accelerator group to the toplevel window
        accelgroup = uimanager.get_accel_group()
        self.add_accel_group(accelgroup)
        return uimanager
