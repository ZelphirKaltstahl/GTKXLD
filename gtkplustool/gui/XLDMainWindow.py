# -*- coding: utf-8 -*-
from gi.repository import Gtk
from gui.XLDMenuBar import XLDMenuBar

__author__ = 'xiaolong'


class XLDMainWindow(Gtk.Window):

    WINDOW_TITLE = 'Xiaolong Dictionary'
    DEFAULT_X_SIZE = 400
    DEFAULT_Y_SIZE = 300
    menubar = None
    uimanager = None

    def __init__(self):
        # super().__init__(title='Xiaolong Dictionary')
        super(XLDMainWindow, self).__init__(title=self.WINDOW_TITLE)

        self.set_default_size(self.DEFAULT_X_SIZE, self.DEFAULT_Y_SIZE)

        self.initialize_widgets()
        self.add_widgets()

    def initialize_widgets(self):
        self.create_ui_manager()
        self.menubar = XLDMenuBar(self)

    def add_widgets(self):
        self.add_menubar()

    def add_menubar(self):
        menubar = self.uimanager.get_widget("/MenuBar")
        box = Gtk.VBox()
        box.pack_start(child=menubar, expand=False, fill=False, padding=0)
        self.add(box)

    def connect_signals(self):
        pass

    def create_ui_manager(self):
        """This method creates a Gtk.UIManager."""
        self.uimanager = Gtk.UIManager()

        # Add the accelerator group to the toplevel window
        accelgroup = self.uimanager.get_accel_group()
        self.add_accel_group(accelgroup)

        return self.uimanager
