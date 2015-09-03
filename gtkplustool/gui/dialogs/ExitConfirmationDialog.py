# -*- coding: utf-8 -*-
from gi.repository import Gtk

__author__ = 'xiaolong'


class ExitConfirmationDialog(Gtk.Dialog):
    def __init__(self, parent):
        title = 'Confirm Exit'
        mode = Gtk.DialogFlags.MODAL
        buttons = (
            'Yes', Gtk.ResponseType.YES,
            'No', Gtk.ResponseType.NO
        )
        Gtk.Dialog.__init__(self, title, parent, mode, buttons)

        label = Gtk.Label("Do you really want to exit Xiaolong Dictionary?")

        box = self.get_content_area()
        box.add(label)

        self.show_all()
