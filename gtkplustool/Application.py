# -*- coding: utf-8 -*-
__author__ = 'xiaolong'

from gi.repository import Gtk
import sys
from AppSettings import AppSettings
import GTKSignal
from VocableManager import VocableManager
from gui.XLDMainWindow import XLDMainWindow
from gui.dialogs.ExitConfirmationDialog import ExitConfirmationDialog


class Application:
    xld_main_window = None

    def __init__(self):
        self.run_application()

    def run_application(self):
        AppSettings.load_settings()

        VocableManager.load_vocables()

        self.xld_main_window = XLDMainWindow()
        Gtk.main()
