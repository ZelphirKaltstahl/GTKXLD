# -*- coding: utf-8 -*-
import os
from os.path import dirname, join

__author__ = 'xiaolong'

MAIN_DIRECTORY = dirname(dirname(dirname(__file__)))


def get_path_of_file(file):
    return os.path.dirname(os.path.realpath(__file__)) + '/'


def go_up(path):
    return path[:path[:path.rfind('/')].rfind('/')] + '/'


def go_in(path, subfolder):
    return path + subfolder + '/'


def get_full_path(*path):
    return join(MAIN_DIRECTORY, *path)
