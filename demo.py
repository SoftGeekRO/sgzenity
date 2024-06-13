#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import random
import time

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import GLib, Gtk

from src.sgzenity.sgszenity import progress_bar, question

counter = 0
_max = 1


def callback_progress_bar(fraction=None):
    global counter
    counter += 0.01
    if counter <= _max:
        return counter
    return True


def demo_progress_bar():
    progress = progress_bar(
        "DEMO TITLE", "DEMO TEXT", False, callback_progress_bar, 350, 30, 10
    )

    progress.run_progressbar()


demo_progress_bar()

_error = question(
    "something went wrong", text="Some big text in small space", height=150, width=400
)
# print(_error)
