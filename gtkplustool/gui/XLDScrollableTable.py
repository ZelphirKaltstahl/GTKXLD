# -*- coding: utf-8 -*-
__author__ = 'xiaolong'

from gi.repository import Gtk


class XLDScrollableTable(Gtk.ScrolledWindow):
    def __init__(
        self,
        treeview,
        hscrollbar_policy=Gtk.PolicyType.AUTOMATIC,
        vscrollbar_policy=Gtk.PolicyType.AUTOMATIC
    ):
        super().__init__()
        self.set_policy(
            hscrollbar_policy=hscrollbar_policy,
            vscrollbar_policy=vscrollbar_policy
        )
        self.add(treeview)
