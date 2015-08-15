import pytest as pytest

from gi.repository import Gtk
from gi.repository import Wnck

from GTKGUITestHelper import GTKGUITestHelper
import GTKSignal
from gui.XLDMainWindow import XLDMainWindow

__author__ = 'xiaolong'


class TestTemplate:

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

    @pytest.fixture()
    def create_xld_main_window(self):
        self.xld_main_window = XLDMainWindow()
        self.xld_main_window.connect(GTKSignal.DELETE, Gtk.main_quit)
        self.xld_main_window.show_all()
        GTKGUITestHelper.refresh_gui()