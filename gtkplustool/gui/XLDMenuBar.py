# -*- coding: utf-8 -*-
import GTKSignal

__author__ = 'xiaolong'

from gi.repository import Gtk


class XLDMenuBar(Gtk.MenuBar):
    MENUBAR_UI_INFO = """<ui>
            <menubar name='xld_menu_bar'>
                <menu action='FileMenu'>

                    <menu action='File_New'>
                        <menuitem action='File_New_Dictionary' />
                    </menu>

                    <!--<separator />-->

                    <menuitem action='File_Open' />

                    <menuitem action='File_Save' />

                    <menu action='File_SaveAs'>
                        <menuitem action='File_SaveAs_Dictionary' />
                        <menuitem action='File_SaveAs_SearchResult' />
                        <menuitem action='File_SaveAs_SelectedVocables' />
                    </menu>

                    <menuitem action='File_Exit' />

                </menu>
            </menubar>
        </ui>"""

    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.toplevel_menubar_action_group = Gtk.ActionGroup("toplevel_menubar_action_group")

        self.initialize_file_menu()
        self.add_file_menu()
        self.add_menu_action_handlers()

        # TODO: add other actions, so far only file menu

        self.load_ui_info()

    def initialize_file_menu(self):
        self.action_filemenu = Gtk.Action(name='FileMenu', label='File', tooltip='opens the file menu', stock_id=None)

        # file -> new
        self.action_filemenu_new = Gtk.Action(name='File_New', label='New', tooltip=None, stock_id=None)
        self.action_filemenu_new_dictionary = Gtk.Action(
            name='File_New_Dictionary',
            label='New dictionary …',
            tooltip='opens the dialog for creating a new dictionary',
            stock_id=None
            # stock_id=Gtk.STOCK_NEW
        )

        # file -> open
        self.action_filemenu_open = Gtk.Action(
            name='File_Open',
            label='Open …',
            tooltip='opens the dialog for opening files',
            # stock_id=Gtk.STOCK_OPEN
            stock_id=None
        )

        # file -> save
        self.action_filemenu_save = Gtk.Action(
            name='File_Save',
            label='Save',
            tooltip='saves current changes of the dictionary to the dictionary file',
            stock_id=None
            # stock_id=Gtk.STOCK_SAVE
        )

        # file -> saveas
        self.action_filemenu_saveas = Gtk.Action(name='File_SaveAs', label='Save As', tooltip=None, stock_id=None)
        self.action_filemenu_saveas_dictionary = Gtk.Action(
            name='File_SaveAs_Dictionary',
            label='Save dictionary as …',
            tooltip='saves the current dictionary with current changes to a specified file',
            # stock_id=Gtk.STOCK_SAVE_AS
            stock_id=None
        )
        self.action_filemenu_saveas_searchresult = Gtk.Action(
            name='File_SaveAs_SearchResult',
            label='Save search result as …',
            tooltip='saves the current search result to a specified file',
            # stock_id=Gtk.STOCK_SAVE_AS
            stock_id=None
        )
        self.action_filemenu_saveas_selectedvocables = Gtk.Action(
            name='File_SaveAs_SelectedVocables',
            label='Save selected vocables as …',
            tooltip='saves the currently selected vocables to a specified file',
            # stock_id=Gtk.STOCK_SAVE_AS
            stock_id=None
        )

        # file -> exit
        self.action_filemenu_exit = Gtk.Action(
            name='File_Exit',
            label='Exit',
            tooltip='Closes the application',
            # stock_id=Gtk.STOCK_QUIT
            stock_id=None
        )

    def add_file_menu(self):
        self.toplevel_menubar_action_group.add_action(self.action_filemenu)
        self.toplevel_menubar_action_group.add_action(self.action_filemenu_new)
        self.toplevel_menubar_action_group.add_action_with_accel(action=self.action_filemenu_new_dictionary, accelerator=None)
        self.toplevel_menubar_action_group.add_action(self.action_filemenu_open)
        self.toplevel_menubar_action_group.add_action(self.action_filemenu_save)
        self.toplevel_menubar_action_group.add_action(self.action_filemenu_saveas)
        self.toplevel_menubar_action_group.add_action(self.action_filemenu_saveas_dictionary)
        self.toplevel_menubar_action_group.add_action(self.action_filemenu_saveas_searchresult)
        self.toplevel_menubar_action_group.add_action(self.action_filemenu_saveas_selectedvocables)
        self.toplevel_menubar_action_group.add_action(self.action_filemenu_exit)

    def add_menu_action_handlers(self):
        self.action_filemenu_new_dictionary.connect(GTKSignal.ACTIVATE, lambda widget: print('You\'ve clicked \"New dictionary\"!'))
        self.action_filemenu_exit.connect(GTKSignal.ACTIVATE, lambda widget: print('You\'ve clicked Exit!'))
        # TODO: add other action handlers

    def load_ui_info(self):
        uimanager = self.parent.uimanager
        uimanager.add_ui_from_string(self.MENUBAR_UI_INFO)
        uimanager.insert_action_group(self.toplevel_menubar_action_group)
