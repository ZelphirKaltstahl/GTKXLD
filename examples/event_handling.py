# -*- coding: utf-8 -*-

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
        self.button_handler_id = self.button_handler_id = self.connect_widget_and_event(
            self.button,
            GTKSignal.CLICKED,
            self.on_button_click
        )
        self.add(self.button)

    def on_button_click(self, widget, data=None):
        print('This Button works only once.')
        if widget is not None:
            print('Clicked Widget:', widget)
        if data is not None:
            print('data=', data, sep=' ', end='\n')
        print('Hello World!')

        # self.disconnect_widget_and_event_by_handler_id(widget, self.button_handler_id)
        self.disconnect_widget_and_event_by_callback(
            widget,
            self.on_button_click
        )


    def connect_widget_and_event(self, widget, event, callback):
        # return the handler_id
        return widget.connect(event, callback)

    def disconnect_widget_and_event_by_handler_id(self, widget, handler_id):
        widget.disconnect(handler_id)

    def disconnect_widget_and_event_by_callback(self, widget, callback):
        widget.disconnect_by_func(callback)

# invoking code
win = MyWindow()
win.connect(GTKSignal.DELETE, Gtk.main_quit)
win.show_all()
Gtk.main()