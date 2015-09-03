# -*- coding: utf-8 -*-
from gi.repository import Gdk
from gi.repository import Gtk
import sys
from AppSettings import AppSettings
import GTKSignal
from VocableManager import VocableManager
from filetools.path_helper import get_full_path
from gui.XLDMenuBar import XLDMenuBar
from gui.dialogs.ExitConfirmationDialog import ExitConfirmationDialog
from gui.notebookpages.DictionaryPage import XLDDictionaryPage
from gui.notebookpages.TrainingPage import TrainingPage

__author__ = 'xiaolong'


class XLDMainWindow(Gtk.Window):
    WINDOW_TITLE = 'Xiaolong Dictionary'
    DEFAULT_X_SIZE = 640
    DEFAULT_Y_SIZE = 480

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
        self.connect_signals()

        self.show_all()

    def initialize_widgets(self):
        self.widget_content_vbox = Gtk.VBox()
        self.create_ui_manager()

    def add_widgets(self):
        self.add(self.widget_content_vbox)
        self.add_menubar()
        self.add_notebook()

    def add_menubar(self):
        self.menubar = XLDMenuBar(self)
        self.menubar.set_name('xld_menu_bar')

        menubar_ui = self.uimanager.get_widget("/xld_menu_bar")
        self.widget_content_vbox.pack_start(child=menubar_ui, expand=False, fill=False, padding=0)

    def add_notebook(self):
        self.notebook = Gtk.Notebook()
        self.notebook.set_name('notebook')

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
        self.connect(GTKSignal.DELETE, self.exit_application)

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

    def exit_application(self, widget, event):
        exit_confirmation_dialog = ExitConfirmationDialog(self)
        exit_confirmation_response = exit_confirmation_dialog.run()

        if exit_confirmation_response == Gtk.ResponseType.YES:
            print("Clicked YES")
            # TODO: Ask if save or not
            VocableManager.save_vocables(VocableManager.vocables)
            AppSettings.save_settings()
            Gtk.main_quit()
            sys.exit()
        elif exit_confirmation_response == Gtk.ResponseType.NO:
            print("Clicked NO")

        exit_confirmation_dialog.destroy()
        return GTKSignal.DO_NOT_PROPAGATE
