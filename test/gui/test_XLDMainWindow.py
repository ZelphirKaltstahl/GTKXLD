from gi.overrides.Gdk import Gdk
import pytest as pytest

from gi.repository import Gtk
from gi.repository import Wnck
from AppSettings import AppSettings

from ..GTKGUITestHelper import GTKGUITestHelper
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

    @pytest.mark.usefixtures('create_xld_main_window')
    def test_window_created(self):
        """This test tests, whether or not the Gtk.Window has been created.
        """
        screen = Wnck.Screen.get_default()
        screen.force_update()  # recommended per Wnck documentation
        window_list = screen.get_windows()

        for window in window_list:
            print(window.get_name())
            if window.has_name():
                if window.get_name() == self.xld_main_window.get_title():
                    window_found = True
                    break
        assert window_found, 'The Gtk.Window named {window_name} has not been found.'\
            .format(window_name=self.xld_main_window.get_title())

        # clean up Wnck (saves resources, check documentation)
        window = None
        screen = None
        # Wnck.shutdown()

    @pytest.mark.usefixtures('create_xld_main_window')
    def test_xldmainwindow_children_widgets_exist(self):
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

    @pytest.mark.usefixtures('create_xld_main_window')
    def test_delete_signal_creates_confirmation_dialogs(self):
        self.xld_main_window.destroy()
        GTKGUITestHelper.refresh_gui()

        save_vocables_dialog_displayed = False
        for window in GTKGUITestHelper.get_window_list():
            if window.get_name() == 'Confirm Save Vocables':
                print('The window has been found!')
                save_vocables_dialog_displayed = True
                break
        assert save_vocables_dialog_displayed, 'The save vocables on exit confirmation dialog is not displayed.'

    @pytest.fixture()
    def create_xld_main_window(self):
        AppSettings.load_settings()
        VocableManager.load_vocables()
        self.xld_main_window = XLDMainWindow()
        self.xld_main_window.show_all()
        GTKGUITestHelper.refresh_gui()
