# -*- coding: utf-8 -*-

from gi.repository import Gtk

button_names = [
    Gtk.STOCK_ABOUT,
    Gtk.STOCK_ADD,
    Gtk.STOCK_REMOVE,
    Gtk.STOCK_QUIT]
buttons = [Gtk.ToolButton.new_from_stock(name) for name in button_names]

toolbar = Gtk.Toolbar()
for button in buttons:
    toolbar.insert(button, -1)
style_context = toolbar.get_style_context()
style_context.add_class(Gtk.STYLE_CLASS_INLINE_TOOLBAR)

window = Gtk.Window()
window.set_size_request(200, 50)
window.add(toolbar)
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()