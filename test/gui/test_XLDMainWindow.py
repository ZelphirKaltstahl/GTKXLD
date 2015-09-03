import pytest as pytest

from gi.repository import Gtk
from gi.repository import Wnck
from AppSettings import AppSettings

from GTKGUITestHelper import GTKGUITestHelper
import GTKSignal
from VocableManager import VocableManager
from gui.BigCharacterBox import BigCharacterBox
from gui.XLDMainWindow import XLDMainWindow
from gui.XLDMenuBar import XLDMenuBar

__author__ = 'xiaolong'


class TestXLDMainWindow:

    application = None
    xld_main_window = None

    def setup(self):
        pass

    def teardown(self):
        pass

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_window_created(self, create_xld_main_window):
        """This test tests, whether or not the Gtk.Window has been created.
        """
        screen = Wnck.Screen.get_default()
        screen.force_update() # recommended per Wnck documentation

        window_found = False

        # loop all windows
        for window in screen.get_windows():
            if window.has_name():
                if window.get_name() == self.xld_main_window.get_title():
                    window_found = True
        assert window_found, 'The Gtk.Window named {window_name} has not been found.'.format(window_name=self.xld_main_window.get_title())

        # clean up Wnck (saves resources, check documentation)
        window = None
        screen = None
        Wnck.shutdown()

    def test_xldmainwindow_children_widgets_exist(self, create_xld_main_window):
        widgets = GTKGUITestHelper.get_all_descendants(self.xld_main_window)

        xld_menu_bar = GTKGUITestHelper.get_widget_by_name_from_list(widgets, 'xld_menu_bar')
        assert xld_menu_bar is not None, \
            'The ' + XLDMainWindow.__name__ + ' does not have a ' + Gtk.MenuBar.__name__ + ' descendant.'
        assert xld_menu_bar.is_visible(), \
            'The ' + XLDMainWindow.__name__ + ' does not have a visible ' + Gtk.MenuBar.__name__ + ' descendant.'

        notebook = GTKGUITestHelper.get_widget_by_name_from_list(widgets, 'notebook')
        assert notebook is not None, \
            'The ' + XLDMainWindow.__name__ + ' does not have a ' + Gtk.Notebook.__name__ + ' descendant.'
        assert notebook.is_visible(), \
            'The ' + XLDMainWindow.__name__ + ' does not have a visible ' + Gtk.Notebook.__name__ + ' descendant.'

        big_character_box = GTKGUITestHelper.get_widget_by_name_from_list(widgets, 'big_character_box')
        assert big_character_box is not None, \
            'The ' + XLDMainWindow.__name__ + ' does not have a ' + BigCharacterBox.__name__ + ' descendant.'
        assert big_character_box.is_visible(), \
            'The ' + XLDMainWindow.__name__ + ' does not have a visible ' + BigCharacterBox.__name__ + ' descendant.'

        # menubar_exists = False
        # menubar_visible = False
        #
        # notebook_exists = False
        # notebook_visible = False
        #
        # big_character_box_exists = False
        # big_character_box_visible = False
        #
        # for widget in widgets:
        #     if isinstance(widget, Gtk.MenuBar) and widget.get_name() == 'xld_menu_bar':
        #         menubar_exists = True
        #         if widget.is_visible():
        #             menubar_visible = True
        #     if isinstance(widget, Gtk.Notebook) and widget.get_name() == 'notebook':
        #         notebook_exists = True
        #         if widget.is_visible():
        #             notebook_visible = True
        #     if isinstance(widget, BigCharacterBox) and widget.get_name() == 'big_character_box':
        #         big_character_box_exists = True
        #         if widget.is_visible():
        #             big_character_box_visible = True
        #
        # assert menubar_exists, \
        #     'The ' + XLDMainWindow.__name__ + ' does not have a ' + Gtk.MenuBar.__name__ + ' descendant.'
        # assert menubar_visible, \
        #     'The ' + XLDMainWindow.__name__ + ' does not have a visible ' + Gtk.MenuBar.__name__ + ' descendant.'
        #
        # assert notebook_exists, \
        #     'The ' + XLDMainWindow.__name__ + ' does not have a ' + Gtk.Notebook.__name__ + ' descendant.'
        # assert notebook_visible, \
        #     'The ' + XLDMainWindow.__name__ + ' does not have a visible ' + Gtk.Notebook.__name__ + ' descendant.'
        #
        # assert big_character_box_exists, \
        #     'The ' + XLDMainWindow.__name__ + ' does not have a ' + BigCharacterBox.__name__ + ' descendant.'
        #
        # assert big_character_box_visible, \
        #     'The ' + XLDMainWindow.__name__ + ' does not have a visible ' + BigCharacterBox.__name__ + ' descendant.'
        #
        # assert GTKGUITestHelper.get_widget_by_name(self.xld_main_window, 'big_character_box') is not None, 'FAIL'

    @pytest.fixture()
    def create_xld_main_window(self):
        AppSettings.load_settings()
        VocableManager.load_vocables()
        self.xld_main_window = XLDMainWindow()
        self.xld_main_window.connect(GTKSignal.DELETE, Gtk.main_quit)
        self.xld_main_window.show_all()
        GTKGUITestHelper.refresh_gui()

    # TODO: Are the widgets styled the way they should be?