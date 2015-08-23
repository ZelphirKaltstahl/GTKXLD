# -*- coding: utf-8 -*-
from gi.repository import Gtk

__author__ = 'xiaolong'


class ImageButton(Gtk.Box):

    image = None

    def __init__(self, image_path=None):
        super().__init__()
        self.image = Gtk.Image()
        self.image.set_from_file(image_path)
        self.add(self.image)