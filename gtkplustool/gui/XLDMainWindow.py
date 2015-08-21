# -*- coding: utf-8 -*-
from gi.repository import Gtk
from gui.XLDMenuBar import XLDMenuBar
from gui.XLDVocableTreeView import XLDVocableTreeView
from helpers.StringHelper import get_leading_zero_number_string, len_of_number

__author__ = 'xiaolong'


class XLDMainWindow(Gtk.Window):

    WINDOW_TITLE = 'Xiaolong Dictionary'
    DEFAULT_X_SIZE = 400
    DEFAULT_Y_SIZE = 300

    widget_content_vbox = None
    menubar = None
    scrolled_window = None
    xld_vocabletreeview = None
    uimanager = None

    def __init__(self):
        # super().__init__(title='Xiaolong Dictionary')
        super(XLDMainWindow, self).__init__(title=self.WINDOW_TITLE)

        self.set_default_size(self.DEFAULT_X_SIZE, self.DEFAULT_Y_SIZE)

        self.initialize_widgets()
        self.add_widgets()

    def initialize_widgets(self):
        self.widget_content_vbox = Gtk.VBox()
        self.create_ui_manager()
        self.menubar = XLDMenuBar(self)

        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.set_policy(
            hscrollbar_policy=Gtk.PolicyType.AUTOMATIC,
            vscrollbar_policy=Gtk.PolicyType.AUTOMATIC
        )
        self.xld_vocabletreeview = XLDVocableTreeView()

    def add_widgets(self):
        self.add(self.widget_content_vbox)
        self.add_menubar()
        self.add_xldvocabletreeview()

    def add_menubar(self):
        menubar = self.uimanager.get_widget("/MenuBar")
        self.widget_content_vbox.pack_start(child=menubar, expand=False, fill=False, padding=0)
        # self.widget_content_grid.attach(child=box, left=1, top=0, width=1, height=1)

    def add_xldvocabletreeview(self):
        sortable_vocable_tree_view_model = self.create_sortable_vocable_tree_view_model()
        self.xld_vocabletreeview.set_model(sortable_vocable_tree_view_model)
        self.scrolled_window.add(self.xld_vocabletreeview)
        self.widget_content_vbox.add(self.scrolled_window)

    def create_sortable_vocable_tree_view_model(self):
        # create the model
        vocable_tree_view_model = Gtk.ListStore(str, str, str, str, str) # index, fl, flps, slps, sl
        vocable_list = [
            ('Hallo','---','---','你好'),
            ('Guten Morgen','---','---','早上好'),
            ('Guten Abend','---','---','晚上好'),
            ('Auf Wiedersehen','---','---','再见'),
            ('Auf Wiedersehen','---','---','再见'),
            ('Auf Wiedersehen','---','---','再见'),
            ('Auf Wiedersehen','---','---','再见'),
            ('Auf Wiedersehen','---','---','再见'),
            ('Auf Wiedersehen','---','---','再见'),
            ('Auf Wiedersehen','---','---','再见'),
            ('Auf Wiedersehen','---','---','再见'),
            ('Auf Wiedersehen','---','---','再见'),
            ('Auf Wiedersehen','---','---','再见'),
            ('Auf Wiedersehen','---','---','再见'),
            ('Auf Wiedersehen','---','---','再见'),
            ('Auf Wiedersehen','---','---','再见'),
            ('Auf Wiedersehen','---','---','再见！你今天有时间吗？'),
            ('essen (v.)','---','---','吃饭')
        ]
        for list_index, vocable in enumerate(vocable_list):
            string_index = get_leading_zero_number_string(list_index, len_of_number(len(vocable_list)))
            row = [string_index]
            for attribute in vocable:
                row.append(attribute)
            vocable_tree_view_model.append(row)

        # make it sortable
        sortable_vocable_tree_view_model = Gtk.TreeModelSort(model=vocable_tree_view_model)

        return sortable_vocable_tree_view_model

    def connect_signals(self):
        pass

    def create_ui_manager(self):
        """This method creates a Gtk.UIManager."""
        self.uimanager = Gtk.UIManager()

        # Add the accelerator group to the toplevel window
        accelgroup = self.uimanager.get_accel_group()
        self.add_accel_group(accelgroup)

        return self.uimanager
