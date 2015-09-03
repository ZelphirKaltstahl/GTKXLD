# -*- coding: utf-8 -*-
from gi.repository import Gtk
from AppSettings import AppSettings

__author__ = 'xiaolong'


class SaveVocablesBeforeExitConfirmationDialog(Gtk.Dialog):
    def __init__(self, parent):
        title = 'Confirm Save Vocables'
        mode = Gtk.DialogFlags.MODAL
        buttons = (
            'Yes', Gtk.ResponseType.YES,
            'No', Gtk.ResponseType.NO
        )
        super().__init__(title, parent, mode, buttons)

        label = Gtk.Label('There are changes to the vocables of the currently opened dictionary.'
                          '\nDo you wish to save those changes?')

        box = self.get_content_area()
        box.add(label)
        self.ask_me_again_checkbutton = Gtk.CheckButton('remember my decision')
        self.ask_me_again_checkbutton.set_active(
            not bool(AppSettings.get_setting_by_name(AppSettings.DIALOG_SHOW_SAVE_VOCABLES_CONFIRMATION_SETTING_NAME))
        )
        box.add(self.ask_me_again_checkbutton)

        self.ask_me_again_checkbutton.connect('toggled', self.save_settings)

        self.show_all()

    def save_settings(self, widget):
        AppSettings.set_setting_by_name(
            AppSettings.DIALOG_SHOW_SAVE_VOCABLES_CONFIRMATION_SETTING_NAME,
            not self.ask_me_again_checkbutton.get_active()
        )
