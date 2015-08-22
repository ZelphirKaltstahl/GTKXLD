# -*- coding: utf-8 -*-

#  Copyright 2015 John Coppens <john@jcoppens.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

from gi.repository import Gtk


class MyPopup(Gtk.MenuButton):
    def __init__(self, btndefs):
        super(MyPopup, self).__init__()

        self.menu = Gtk.Menu()
        self.set_popup(self.menu)
        self.set_label(">>")
        self.set_direction(Gtk.ArrowType.RIGHT)

        for btndef in btndefs:
            if len(btndef) == 1:  # This is a normal button
                item = Gtk.MenuItem()
                item.set_label(btndef[0])
                item.show()
                self.menu.append(item)
            else:
                group = None
                for radiodef in btndef:  # It's a selection of radiobuttons
                    item = Gtk.RadioMenuItem(label=radiodef)
                    if group is None:
                        group = item
                    else:
                        item.set_property("group", group)
                    item.show()
                    self.menu.append(item)


class MainWindow(Gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.set_size_request(200, -1)
        self.connect("destroy", lambda x: Gtk.main_quit())

        self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.entry = Gtk.Entry()

        self.popup = MyPopup((("String", "String no case", "Hexadecimal"),
                              ("Regexp",)))

        self.hbox.pack_start(self.entry, True, True, 0)
        self.hbox.pack_start(self.popup, False, True, 0)

        self.add(self.hbox)

        self.show_all()

    def run(self):
        Gtk.main()


def main():
    mw = MainWindow()
    mw.run()
    return 0


if __name__ == '__main__':
    main()
