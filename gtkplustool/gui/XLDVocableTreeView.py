# -*- coding: utf-8 -*-
from gi.repository import Gtk

import GTKSignal
from VocableManager import VocableManager
from gui.popupmenus.PopupMenuProvider import PopupMenuProvider

__author__ = 'xiaolong'

GUI_POPUP_MENU_INFO = """
<ui>
    <popup name='VocableTreeViewPopupMenu'>
        <menuitem action='VocableTreeViewPopupMenu_Training' />
        <menuitem action='VocableTreeViewPopupMenu_Change' />
        <menuitem action='VocableTreeViewPopupMenu_Delete' />
    </popup>
</ui>
"""


class XLDVocableTreeView(Gtk.TreeView):
    column_expand = [False, True, False, False, True]
    columns_titles = ['#', 'German', 'IPA', 'Pīnyīn', 'Mandarin']
    columns = []
    cell_renderers = []

    popup_menu_ui = None
    popup_menu_action_group = None
    action_popup_training = None
    action_popup_change = None
    action_popup_delete = None

    click_counter = 0

    vocable_selection_listeners = []

    def __init__(self, model=None):
        super().__init__(model=model)

        for index, column_title in enumerate(self.columns_titles):
            # create Gtk.TreeViewColumns
            self.columns.append(Gtk.TreeViewColumn(title=column_title))
            # add Gtk.TreeViewColumns to the TreeView
            self.append_column(self.columns[-1])
            # create Gtk.CellRendererTexts
            self.cell_renderers.append(Gtk.CellRendererText())
            # style the CellRendererTexts
            self.cell_renderers[-1].set_alignment(xalign=0.0, yalign=0.0)
            # ???
            self.columns[-1].pack_start(self.cell_renderers[-1], self.column_expand[index])

            self.columns[-1].add_attribute(
                cell_renderer=self.cell_renderers[-1],
                attribute='text',
                column=index
            )

            self.set_search_column(index)
            self.columns[-1].set_sort_column_id(index)
            self.columns[-1].set_reorderable(True)

        self.get_selection().set_mode(Gtk.SelectionMode.MULTIPLE)

        self.connect_signal_handlers()
        self.connect_selection_signal_handlers()

        # popup menu on right click
        self.popup_menu_ui = PopupMenuProvider.get_vocable_treeview_popup_menu()

    def connect_signal_handlers(self):
        self.connect(GTKSignal.CLICK, self.on_button_press_event)

    def connect_selection_signal_handlers(self):
        self.get_selection().connect('changed', self.notify_vocable_selection_listeners)

    def on_button_press_event(self, widget, event):
        if event.button == GTKSignal.RIGHT_MOUSE_BUTTON_ID:
            self.popup_menu_ui.popup(
                parent_menu_shell=None,
                parent_menu_item=None,
                func=None,
                data=None,
                button=event.button,
                activate_time=event.time
            )
        # elif event.button == GTKSignal.LEFT_MOUSE_BUTTON_ID:
        #     self.notify_vocable_selection_listeners()

            # if event.type == Gdk.EventType.TRIPLE_BUTTON_PRESS:
            #     print('You tripple clicked!')
            #
            # elif event.type == Gdk.EventType.DOUBLE_BUTTON_PRESS:
            #     print('You double clicked!')
            #
            # elif event.type == Gdk.EventType.BUTTON_PRESS:
            #     print('You single clicked!')

            return GTKSignal.DO_NOT_PROPAGATE

    def register_vocable_selection_listeners(self, listener):
        self.vocable_selection_listeners.append(listener)

    def notify_vocable_selection_listeners(self, tree_selection):
        vocable = self.get_vocable_from_tree_selection(tree_selection)
        print('Vocable:', vocable)
        for vocable_selection_listener in self.vocable_selection_listeners:
            vocable_selection_listener.update(vocable)

    def get_vocable_from_tree_selection(self, tree_selection):
        vocable_index = -1
        (model, pathlist) = tree_selection.get_selected_rows()
        # print(tree_selection.get_selected()) # not for SELECTION_MULTIPLE
        print('pathlist:', pathlist)
        if pathlist is not None and len(pathlist) == 1:
            vocable_index = int(str(pathlist[0]))

            # for path in pathlist:
            #     print('path:', int(str(path)))
            #     print('type of path:', type(path))
            #     print('row object:', model[path])
            #     print('row object iter:', model[path].iter)
            #     print('row object iter DIR:', dir(model[path].iter))
            #     print('row objecct iter repr:', repr(model[path].iter))
            #     print('row index:', model[path][0]) # [column_number_that_you_want]
            #     print('row list', list(model[path]))

        # for path in pathlist :
        #     print('Path:', path)
        #
        #     tree_iter = model.get_iter(path)
        #     print('Tree Iter:', tree_iter)
        #
        #     value = model.get_value(tree_iter)
        #     print(value)
        return VocableManager.get_search_result_vocable(vocable_index)
