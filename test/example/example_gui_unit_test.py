# -*- coding: utf-8 -*-
import time

__author__ = 'xiaolong'

from unittest import TestCase, main
from gi.repository import Gtk

from test.GTKGUITestHelper import GTKGUITestHelper


class MyView(Gtk.VBox):
    def __init__(self):
        super(MyView, self).__init__()
        self._button = Gtk.Button('Click Me')
        self._label = Gtk.Label()
        self.pack_start(child=self._button, expand=0, fill=0, padding=0)
        self.pack_start(child=self._label, expand=0, fill=0, padding=0)
        self._count = 0
        self._button.connect('clicked', self.on_button_clicked)

    def on_button_clicked(self, button):
        self._count = self._count + 1
        self._label.set_text('clicked %s times' % self._count)


class MyViewTest(TestCase):
    def setUp(self):
        self._v = MyView()

    def test_count(self):
        self.assertEqual(self._v._count, 0)
        self._v._button.clicked()
        GTKGUITestHelper.refresh_gui()
        self.assertEqual(self._v._count, 1)

    def test_label(self):
        self._v._button.clicked()
        GTKGUITestHelper.refresh_gui()
        self.assertEqual(self._v._label.get_text(), 'clicked 1 times')

if __name__ == '__main__':
    main()
