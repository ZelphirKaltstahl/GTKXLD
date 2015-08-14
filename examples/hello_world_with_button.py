# -*- coding: utf-8 -*-
from gtkplustool.GTKSignal import CLICKED, DELETE

__author__ = 'xiaolong'

from gi.repository import Gtk
from gtkplustool import GTKSignal

class MyWindow(Gtk.Window):

    button = None
    button_handler_id = None

    def __init__(self):
        # super constructor call
        Gtk.Window.__init__(self, title='Hello World')
        self.add_widgets()

    def add_widgets(self):
        self.button = Gtk.Button(label='Click me!')
        self.button_handler_id = self.button.connect(CLICKED, self.on_button_click, ['a'])
        self.add(self.button)

    def on_button_click(self, widget, data=None):
        if data is None:
            print('You clicked the button!')
        else:
            print('You clicked the button and the data is', data)
        print('I\'ll now disconnect the button and the event from each other')
        widget.disconnect(self.button_handler_id)
        print('You may try to click again, but don\'t expect me to react!')

        if not self.button.handler_is_connected(self.button_handler_id):
            print('OK, OK ..., I\'ll connect the two of them again!')
            widget.connect(CLICKED, self.on_button_click)
        else:
            print('But I can also disconnect them using the callback function!')
            widget.disconnect_by_func(self.on_button_click)

# invoking code
win = MyWindow()
win.connect(DELETE, Gtk.main_quit)
win.show_all()
Gtk.main()