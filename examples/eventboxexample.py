# -*- coding: utf-8 -*-
from gi.repository import Gtk


def cb(widget, event, data):
    if event.button != 3:
        return False
    m = Gtk.Menu()
    i = Gtk.MenuItem("Hello")
    i.show()
    m.append(i)
    m.popup(None, None, None, event.button, event.time, None)
    return False


win = Gtk.Window()
win.connect("delete_event", Gtk.main_quit)

eb = Gtk.EventBox()
win.add(eb)
eb.connect("button_press_event", cb, None)
eb.show()

win.show()

Gtk.main()
