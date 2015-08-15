# -*- coding: utf-8 -*-
from gi.repository import Gtk
import time

__author__ = 'xiaolong'


class GTKGUITestHelper():
    def __init__(self):
        pass

    @classmethod
    def refresh_gui(cls, delay=0):
        #print('delay', delay)
        while Gtk.events_pending():
            Gtk.main_iteration_do(blocking=False)
        time.sleep(float(delay))
