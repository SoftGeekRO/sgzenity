#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import time

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import GLib, GObject, Gtk

from src.sgzenity.SGProgresBar import ProgressBar
from src.sgzenity.sgszenity import calendar, question
from src.sgzenity.thread import WorkerThread


class WorkingThread(WorkerThread):
    def payload(self):
        loading = self.data
        steps = 10
        for s in range(steps):
            if self.stop:
                break
            loading.heartbeat()
            print('Pulse {}.'.format(s))
            time.sleep(1)
        if self.stop:
            print('Working thread canceled.')
        else:
            print('Working thread ended.')
        loading.close()


def sg_progress_bar():

    loading = ProgressBar("DEMO TITLE", "DEMO TEXT", pulse_mode=True)

    workthread = WorkingThread(loading)
    loading.show(workthread)
    workthread.start()

    Gtk.main()


sg_progress_bar()

_error = question(
    "something went wrong", text="Some big text in small space", height=150, width=400
)

_calendar = calendar("DEMO CALENDAR")
print(_calendar)
