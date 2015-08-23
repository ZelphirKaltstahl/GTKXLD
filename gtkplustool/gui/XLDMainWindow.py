# -*- coding: utf-8 -*-
from gi.repository import Gdk
from gi.repository import Gtk
from filetools.path_helper import get_full_path
from gui.XLDMenuBar import XLDMenuBar
from gui.XLDVocableTreeView import XLDVocableTreeView
from gui.notebookpages.DictionaryPage import XLDDictionaryPage
from gui.notebookpages.TrainingPage import TrainingPage
from helpers.StringHelper import get_leading_zero_number_string, len_of_number

__author__ = 'xiaolong'


class XLDMainWindow(Gtk.Window):
    WINDOW_TITLE = 'Xiaolong Dictionary'
    DEFAULT_X_SIZE = 400
    DEFAULT_Y_SIZE = 300

    style_provider = None

    widget_content_vbox = None
    menubar = None

    notebook = None
    dictionary_page = None
    training_page = None

    scrolled_window = None
    xld_vocabletreeview = None

    uimanager = None

    def __init__(self):
        # super().__init__(title='Xiaolong Dictionary')
        super(XLDMainWindow, self).__init__(title=self.WINDOW_TITLE)

        self.set_default_size(self.DEFAULT_X_SIZE, self.DEFAULT_Y_SIZE)

        self.initialize_widgets()
        self.add_widgets()
        self.load_style_sheet()

    def initialize_widgets(self):
        self.widget_content_vbox = Gtk.VBox()
        self.create_ui_manager()

    def add_widgets(self):
        self.add(self.widget_content_vbox)
        self.add_menubar()
        self.add_notebook()

    def add_menubar(self):
        self.menubar = XLDMenuBar(self)
        menubar_ui = self.uimanager.get_widget("/MenuBar")
        self.widget_content_vbox.pack_start(child=menubar_ui, expand=False, fill=False, padding=0)

    def add_notebook(self):
        self.notebook = Gtk.Notebook()
        self.widget_content_vbox.add(self.notebook)
        self.add_xldvocabletreeview_page()
        self.add_training_page()

    def add_xldvocabletreeview_page(self):
        self.dictionary_page = XLDDictionaryPage()
        self.notebook.append_page(self.dictionary_page, Gtk.Label('Dictionary'))

    def add_training_page(self):
        # page is a grid
        self.training_page = TrainingPage()

        # append page to notebook
        self.notebook.append_page(self.training_page, Gtk.Label('Training'))

    def connect_signals(self):
        pass

    def create_ui_manager(self):
        """This method creates a Gtk.UIManager."""
        self.uimanager = Gtk.UIManager()

        # Add the accelerator group to the toplevel window
        accelgroup = self.uimanager.get_accel_group()
        self.add_accel_group(accelgroup)

        return self.uimanager

    '''
    def on_button_press_event(self, widget, event):
        if event.type == Gdk.EventType.BUTTON_PRESS and event.button == 3:
            print('You right-clicker!')
                '''

    def load_style_sheet(self):
        if self.style_provider is None:
            self.style_provider = Gtk.CssProvider()

        self.style_provider.load_from_path(get_full_path('res/css', 'style.css'))

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            self.style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
