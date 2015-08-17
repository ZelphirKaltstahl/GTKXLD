# -*- coding: utf-8 -*-detailed_signal (str) –
handler

from gi.repository import Gtk
"""This example shows how to react on a right click on a Cell in a TreeView.
However there is a small problem with the code.
It always prints the previously selected Cell index."""


class Test(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        store = Gtk.ListStore(str)
        self.tree = Gtk.TreeView(store)
        for i in range(0, 10):
            store.append(["test " + str(i)])
        self.connect("delete-event", Gtk.main_quit)
        self.tree.connect("button_press_event", self.mouse_click)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Title", renderer, text=0)
        self.tree.append_column(column)
        self.add(self.tree)

    def mouse_click(self, tv, event):
        if event.button == 3:
            selection = self.tree.get_selection()
            # selection = self.tree.get_cursor()
            (model, itera) = selection.get_selected()
            # (model, itera) = self.tree.get_cell_area(selection)
            print(model[itera][0])


win = Test()
win.show_all()
Gtk.main()
