import time

import gi

gi.require_version('Gtk', '3.0')
from functools import partial

from gi.repository import GLib, GObject, Gtk

from .base import Base
from .thread import WorkerThread


class SGProgressBar(Base):

    def __init__(self, title, text, pulse_mode=False, callback=None, *args, **kwargs):
        super().__init__(**kwargs)

        self.title = title
        self.text = text
        self.show_text = True if self.text else False
        self.pulse_mode = pulse_mode
        self.callback = callback

        self.dialog = Gtk.ProgressBar()
        self.vbox.pack_start(self.dialog, True, True, 0)

        self.timeout_id = GLib.timeout_add(50, self.update_progress, None)

        self.init_progressbar()

        # Start the background thread.
        self.worker = WorkerThread(self)
        self.worker.start()

    def run_progressbar(self):
        GObject.threads_init()
        self.show_all()
        Gtk.main()

    def refresh_in_thread(self):
        GObject.idle_add(self.update_progress)

    def init_progressbar(self):
        # global config for progress bar
        self.set_border_width(10)
        self.set_resizable(False)
        self.set_default_size(self.width, self.height)

        if self.pulse_mode:
            self.dialog.pulse()
        else:
            self.dialog.set_fraction(0.0)

        if self.title:
            self.set_title(self.title)

        if self.show_text:
            self.dialog.set_text(self.text)
            self.dialog.set_show_text(self.show_text)

        self.connect("destroy", self._destroy)

    def update_progress(self, progress=None):
        """

        :return:
        """

        callback = self.callback() if callable(self.callback) else None
        if callback >= 1:
            time.sleep(.1)
            self._destroy()

        if self.pulse_mode:
            self.dialog.pulse()
        else:
            self.dialog.set_fraction(callback)
        return False

    def _destroy(self, widget=None):
        self.worker.done = True
        Gtk.main_quit()
