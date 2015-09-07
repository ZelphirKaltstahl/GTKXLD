# -*- coding: utf-8 -*-
from gi.repository import Gtk
from AppSettings import AppSettings

__author__ = 'xiaolong'


class ExitConfirmationDialog(Gtk.Dialog):
    label = None
    remember_decision_checkbutton = None

    def __init__(self, parent):
        title = 'Confirm Exit'
        mode = Gtk.DialogFlags.MODAL
        buttons = (
            'Yes', Gtk.ResponseType.YES,
            'No', Gtk.ResponseType.NO
        )
        super().__init__(title, parent, mode, buttons)

        self.initialize_widgets()
        self.add_widgets()
        self.connect_signals()
        self.show_all()

    def initialize_widgets(self):
        self.label = Gtk.Label('Do you really want to exit Xiaolong Dictionary?')
        self.remember_decision_checkbutton = Gtk.CheckButton('Remember my decision.')
        self.remember_decision_checkbutton.set_active(
            not bool(AppSettings.get_setting_by_name(AppSettings.DIALOG_SHOW_EXIT_CONFIRMATION_SETTING_NAME))
        )

    def add_widgets(self):
        self.get_content_area().add(self.label)
        self.get_content_area().add(self.remember_decision_checkbutton)

    def connect_signals(self):
        self.remember_decision_checkbutton.connect('toggled', self.save_settings)

    def save_settings(self, widget):
        AppSettings.change_setting_by_name(
            AppSettings.DIALOG_SHOW_EXIT_CONFIRMATION_SETTING_NAME,
            not self.remember_decision_checkbutton.get_active()
        )
