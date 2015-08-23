# -*- coding: utf-8 -*-
from gi.repository import Gtk, Gdk
import GTKSignal
from ImageButton import ImageButton
from Settings import SETTINGS
from filetools.path_helper import get_full_path

__author__ = 'xiaolong'


class BigCharacterBox(Gtk.Grid):
    text = '中文'
    character_position = 0

    big_character_label_frame = None
    big_character_label = None
    previous_button = None
    next_button = None

    previous_button_event_box = None
    next_button_event_box = None

    def __init__(self):
        super().__init__()

        self.initialize_widgets()
        self.add_widgets()
        self.connect_signals()

        self.show_all()

    def initialize_widgets(self):
        self.set_row_spacing(4)
        self.set_column_spacing(4)
        self.set_column_homogeneous(True)
        self.set_hexpand(False)

        self.big_character_label_frame = Gtk.Frame(label='Characters')
        self.big_character_label_frame.set_name('bigCharacterLabelFrame')
        self.big_character_label_frame.set_label_align(xalign=0.5, yalign=0.5)

        self.big_character_label = Gtk.Label('')
        self.big_character_label.set_name('bigCharacterLabel')
        self.set_text('中文')

        self.previous_button = Gtk.Button('prev.')
        self.previous_button.set_hexpand(True)

        self.next_button = Gtk.Button('next')
        self.next_button.set_hexpand(True)

    def add_widgets(self):
        self.big_character_label_frame.add(self.big_character_label)
        self.attach(child=self.big_character_label_frame, left=0, top=0, width=2, height=1)
        self.attach(child=self.previous_button, left=0, top=2, width=1, height=1)
        self.attach(child=self.next_button, left=1, top=2, width=1, height=1)

    def connect_signals(self):
        self.previous_button.connect('button-press-event', self.on_previous_button_press)
        self.next_button.connect('button-press-event', self.on_next_button_press)

    def set_text(self, text=''):
        self.text = text
        self.character_position = 0
        self.big_character_label.set_text(text[0])

    def set_character(self, character=' '):
        self.big_character_label.set_text(character)

    def next_character(self):
        next_position = (self.character_position + 1) % len(self.text)
        self.set_character(character=self.text[next_position])
        self.character_position = next_position

    def previous_character(self):
        previous_position = (self.character_position - 1 + len(self.text)) % len(self.text)
        self.set_character(character=self.text[previous_position])
        self.character_position = previous_position

    def on_next_button_press(self, widget, event):
        if event.button == GTKSignal.LEFT_MOUSE_BUTTON_ID:
            if event.type == Gdk.EventType.BUTTON_PRESS:
                self.next_character()
            return GTKSignal.DO_NOT_PROPAGATE

    def on_previous_button_press(self, widget, event):
        if event.button == GTKSignal.LEFT_MOUSE_BUTTON_ID:
            if event.type == Gdk.EventType.BUTTON_PRESS:
                self.previous_character()
            return GTKSignal.DO_NOT_PROPAGATE
