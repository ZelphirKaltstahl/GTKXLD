# -*- coding: utf-8 -*-
from gi.repository import Gtk
from gtkplustool import GTKSignal

__author__ = 'xiaolong'


class CustomWindow(Gtk.Window):

    button = None

    def __init__(self):
        # super constructor call
        Gtk.Window.__init__(self, title='Hello World')
        self.add_widgets()

    def add_widgets(self):
        self.button = Gtk.Button()
        self.button.set_label("Hello World")
        #self.label.set_angle(25)
        # self.label.set_halign(Gtk.Align.CENTER)
        # self.label.set_valign(Gtk.Align.CENTER)
        # self.add(self.label)
        self.button.connect(GTKSignal.CLICKED, lambda widget, data=None: print(widget, 'clicked! Data', data, 'received'))

        alignment = Gtk.Alignment(xalign=0.5, yalign=0.5, xscale=0, yscale=0)
        alignment.add(self.button)
        self.add(alignment)



gtk_window = CustomWindow()
gtk_window.connect(GTKSignal.DELETE, Gtk.main_quit)
gtk_window.show_all()
Gtk.main()