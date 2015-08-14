# -*- coding: utf-8 -*-
__author__ = 'xiaolong'

from gi.repository import Gtk
from gtkplustool import GTKSignal

# creating a new GTK Window
win = Gtk.Window()

# connect the delete signal with the exit function of GTK
win.connect(GTKSignal.DELETE, Gtk.main_quit)

# show the window and all its content
win.show_all()

# start the GTK+ processing loop
Gtk.main()