from gi.repository import Gtk
from gtkplustool import GTKSignal
from gtkplustool.gui.XLDMainWindow import XLDMainWindow

__author__ = 'xiaolong'

if __name__ == '__main__':
    xld_main_window = XLDMainWindow()
    xld_main_window.connect(GTKSignal.DELETE, Gtk.main_quit)
    xld_main_window.show_all()
    Gtk.main()
