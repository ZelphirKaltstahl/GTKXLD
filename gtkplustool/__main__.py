from gi.repository import Gtk
from VocableManager import VocableManager
from gtkplustool import GTKSignal
from gtkplustool.gui.XLDMainWindow import XLDMainWindow

__author__ = 'xiaolong'

if __name__ == '__main__':

    # TODO: Load settings from a settings file

    VocableManager.load_vocables()

    xld_main_window = XLDMainWindow()
    xld_main_window.connect(GTKSignal.DELETE, Gtk.main_quit)
    xld_main_window.show_all()
    Gtk.main()
