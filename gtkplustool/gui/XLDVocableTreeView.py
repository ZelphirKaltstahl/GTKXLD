# -*- coding: utf-8 -*-
from gi.repository import Gtk

__author__ = 'xiaolong'


class XLDVocableTreeView(Gtk.TreeView):

    column_expand = [False, True, False, False, True]
    columns_titles = ['#', 'German', 'IPA', 'Pīnyīn', 'Mandarin']
    columns = []
    cell_renderers = []

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

        self.set_reorderable(True)

    def set_data(self, model):
        self.set_model(model)  # TODO: decide whether or not this is useful
        pass
