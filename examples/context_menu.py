# -*- coding: utf-8 -*-
from gi.repository import Gtk

def show_menu(self, *args):
    i1 = Gtk.MenuItem("Item 1")
    menu.append(i1)
    i2 = Gtk.MenuItem("Item 2")
    menu.append(i2)
    menu.show_all()
    menu.popup(None, None, None, None, 0, Gtk.get_current_event_time())
    print("Done")

window = Gtk.Window()
button = Gtk.Button("Create pop-up")
menu = Gtk.Menu()
button.connect("clicked", show_menu)
window.connect('destroy', Gtk.main_quit)
window.add(button)
window.show_all()
Gtk.main()