# -*- coding: utf-8 -*-
# !/usr/bin/env python

# example basictreeview.py
from gi.repository import Gtk
from random import randint
from math import log10, floor
from helpers.StringHelper import get_leading_zero_number_string, len_of_number


class BasicTreeViewExample:
    # close the window and quit
    def delete_event(self, widget, event, data=None):
        Gtk.main_quit()
        return False

    def __init__(self):
        # Create a new window
        self.window = Gtk.Window()

        self.window.set_title("Basic TreeView Example")

        self.window.set_size_request(200, 200)

        self.window.connect("delete_event", self.delete_event)

        # create a TreeStore with one string column to use as the model
        self.liststore = Gtk.ListStore(str, str)

        # we'll add some data now - 4 rows with 3 child rows each
        list = [x for x in range(1001)]
        for parent_index in range(len(list)):
            # parent_handle = self.liststore.append([str(parent_index), 'aaa {random_string}'.format(random_string=str(randint(0,9)))])
            print(parent_index)
            parent_handle = self.liststore.append(
                [get_leading_zero_number_string(parent_index, len_of_number(len(list))),
                 'aaa {random_string}'.format(random_string=str(randint(0,9)))]
            )
            '''for child_index in range(3):
                self.liststore.append(parent_handle, ['child {child_count} of parent {parent_count}'.format(child_count=child_index, parent_count=parent_index)])'''

        # create the TreeView using treestore
        self.treeview = Gtk.TreeView(model=Gtk.TreeModelSort(model=self.liststore))

        # create the TreeViewColumn to display the data
        self.index_column = Gtk.TreeViewColumn(title='#')
        self.first_language_column = Gtk.TreeViewColumn(title='First Language')

        # add tvcolumn to treeview
        self.treeview.append_column(self.index_column)
        self.treeview.append_column(self.first_language_column)

        # create a CellRendererText to render the data
        self.index_cell_renderer = Gtk.CellRendererText()
        self.index_cell_renderer.set_alignment(xalign=0.0, yalign=0.0)
        self.first_language_cell_renderer = Gtk.CellRendererText()
        # self.first_language_cell_renderer.set_property('xalign', 0.0)
        self.first_language_cell_renderer.set_alignment(xalign=0.5, yalign=0.0)

        # add the cell to the tvcolumn and allow it to expand
        self.index_column.pack_start(self.index_cell_renderer, False)
        self.first_language_column.pack_start(self.first_language_cell_renderer, True)

        # set the cell "text" attribute to column 0 - retrieve text
        # from that column in treestore
        self.index_column.add_attribute(
            cell_renderer=self.index_cell_renderer,
            attribute='text',
            column=0
        )
        self.first_language_column.add_attribute(
            cell_renderer=self.first_language_cell_renderer,
            attribute='text',
            column=1
        )

        # make it searchable
        self.treeview.set_search_column(0)
        self.treeview.set_search_column(1)

        # Allow sorting on the column
        self.index_column.set_sort_column_id(0)
        self.first_language_column.set_sort_column_id(1)

        # Allow drag and drop reordering of rows
        self.treeview.set_reorderable(True)

        self.window.add(self.treeview)

        self.window.show_all()


def main():
    Gtk.main()

'''
def get_index_unformated_string(list):
    return '{0:0'+str(len_of_number(len(list)-1))+'d}'

def len_of_number(number):
    return int(log10(number)+1)
'''
if __name__ == "__main__":
    tvexample = BasicTreeViewExample()
    main()
