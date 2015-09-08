# -*- coding: utf-8 -*-
from gi.repository import Gtk
import time
from gi.repository import Wnck

__author__ = 'xiaolong'


class GTKGUITestHelper:
    def __init__(self):
        pass

    @classmethod
    def refresh_gui(cls, delay=0):
        # print('delay', delay)
        while Gtk.events_pending():
            Gtk.main_iteration_do(blocking=False)
        time.sleep(float(delay))

    @classmethod
    def get_all_descendants(cls, widget):
        widget_stack = [widget]
        descendants = []

        while len(widget_stack) > 0:
            current_widget = widget_stack.pop()
            if current_widget is not widget:
                descendants.append(current_widget)
            if isinstance(current_widget, Gtk.Container):
                for child in current_widget.get_children():
                    widget_stack.append(child)

        return descendants

    @classmethod
    def find_widget_by_name(cls, root_widget, widget_name):
        if root_widget.get_name() == widget_name:
            return root_widget

        widgets = GTKGUITestHelper.get_all_descendants(root_widget)
        for widget in widgets:
            if widget.get_name() == widget_name:
                return widget

        return None

    @classmethod
    def get_widget_by_name_from_list(cls, widget_list, widget_name):
        for widget in widget_list:
            if widget.get_name() == widget_name:
                return widget
        return None

    @classmethod
    def get_window_list(cls):
        screen = Wnck.Screen.get_default()

        # recommended per Wnck documentation
        screen.force_update()

        window_list = screen.get_windows()

        # clean up Wnck (saves resources, check documentation)
        # del window
        del screen
        # Wnck.shutdown()

        print(window_list)

        return window_list
