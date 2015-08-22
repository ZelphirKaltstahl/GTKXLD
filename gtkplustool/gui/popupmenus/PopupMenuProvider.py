# -*- coding: utf-8 -*-
from gi.repository import Gtk
import GTKSignal

__author__ = 'xiaolong'


class PopupMenuProvider():
    uimanager = None

    vocable_treeview_popup_menu_ui = None
    vocable_treeview_popup_menu_action_group = None

    VOCABLE_TREEVIEW_POPUP_MENU = """
        <ui>
            <popup name='VocableTreeViewPopupMenu'>
                <menuitem action='VocableTreeViewPopupMenu_Training' />
                <menuitem action='VocableTreeViewPopupMenu_Change' />
                <menuitem action='VocableTreeViewPopupMenu_Delete' />
            </popup>
        </ui>
    """

    def __init__(self):
        pass

    @classmethod
    def create_uimanager(cls):
        if PopupMenuProvider.uimanager is None:
            PopupMenuProvider.uimanager = Gtk.UIManager()

    @classmethod
    def get_vocable_treeview_popup_menu(cls):
        if PopupMenuProvider.uimanager is None:
            PopupMenuProvider.create_uimanager()

        if PopupMenuProvider.vocable_treeview_popup_menu_action_group is None:
            PopupMenuProvider.create_popup_menu_action_group()

        if PopupMenuProvider.vocable_treeview_popup_menu_ui is None:
            PopupMenuProvider.uimanager.add_ui_from_string(PopupMenuProvider.VOCABLE_TREEVIEW_POPUP_MENU)
            PopupMenuProvider.uimanager.insert_action_group(PopupMenuProvider.vocable_treeview_popup_menu_action_group)
            PopupMenuProvider.vocable_treeview_popup_menu_ui = PopupMenuProvider.uimanager.get_widget("/VocableTreeViewPopupMenu")

        return PopupMenuProvider.vocable_treeview_popup_menu_ui

    @classmethod
    def create_popup_menu_action_group(cls):
        PopupMenuProvider.vocable_treeview_popup_menu_action_group = Gtk.ActionGroup(
            'vocable_treeview_popup_menu_action_group'
        )

        PopupMenuProvider.action_popup_training = Gtk.Action(
            name='VocableTreeViewPopupMenu_Training',
            label='Training',
            tooltip='switches to the training page',
            stock_id=None
        )

        PopupMenuProvider.action_popup_change = Gtk.Action(
            name='VocableTreeViewPopupMenu_Change',
            label='Change',
            tooltip='opens the dialog for changing selected vocables',
            stock_id=None
        )

        PopupMenuProvider.action_popup_delete = Gtk.Action(
            name='VocableTreeViewPopupMenu_Delete',
            label='Delete',
            tooltip='deletes the selected vocables',
            stock_id=None
        )

        PopupMenuProvider.vocable_treeview_popup_menu_action_group.add_action(PopupMenuProvider.action_popup_training)
        PopupMenuProvider.vocable_treeview_popup_menu_action_group.add_action(PopupMenuProvider.action_popup_change)
        PopupMenuProvider.vocable_treeview_popup_menu_action_group.add_action(PopupMenuProvider.action_popup_delete)

        PopupMenuProvider.action_popup_training.connect(GTKSignal.ACTIVATE, lambda widget: print('Training clicked!'))
