import time

import gi

gi.require_version('Gtk', '3.0')
from functools import partial

from gi.repository import GLib, GObject, Gtk

from .thread import WorkerThread

DEFAULT_WIDTH = 300
DEFAULT_HEIGHT = 60
BORDER_WIDTH = 10


class ProgressBar(Gtk.Window):

    def __init__(
        self,
        title,
        text=None,
        pulse_mode=True,
        width=DEFAULT_WIDTH,
        height=DEFAULT_HEIGHT,
        border_width=BORDER_WIDTH,
        parent=None,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.title = title
        self.text = text
        self.pulse_mode = pulse_mode
        self.border_width = border_width
        self.width = width
        self.height = height
        self.pulses = 10
        self._count = 0
        self.workthread = None

        # Create the GUI
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.progressbar = Gtk.ProgressBar()
        vbox.pack_start(self.progressbar, True, True, 0)

        self.timeout_id = GLib.timeout_add(50, self.on_timeout, None)

        self.connect("destroy", self.cancel)

        self.init()

    def init(self):
        self.set_border_width(self.border_width)
        self.set_resizable(False)
        self.set_default_size(self.width, self.height)

        if self.pulse_mode:
            self.progressbar.pulse()
        else:
            self.progressbar.set_fraction(0.0)

        if self.title:
            self.set_title(self.title)

        if self.text:
            self.progressbar.set_text(self.text)
            self.progressbar.set_show_text(True if self.text else False)

        self.connect("destroy", self.cancel)

    def show(self, workthread):
        """Show loading window.
        This needs to be called frm Gtk main thread.

        Show the loading dialog just before starting the workthread.

        :param workthread:
        :return:
        """
        if self.workthread is not None:
            print(
                'There is a workthread active. Please call close() or cancel() before starting a new loading event.'
            )
            return False

        if workthread is not None:
            if not isinstance(workthread, WorkerThread):
                raise Exception('The thread needs to be a subclass of WorkingThread.')
            self.workthread = workthread

        self.show_all()

        return False

    def on_timeout(self, progress=None):
        if self.pulse_mode:
            self.progressbar.pulse()
        else:
            self.progressbar.set_fraction(self._count)
        return self.pulse_mode

    def heartbeat(self, text=None):

        if self.pulse_mode:
            return False

        self._count += 0.1

        if text is None:
            text = '{0:0.1f}%'.format(self._count * 100)

        GLib.idle_add(self.progressbar.set_fraction, self._count)
        GLib.idle_add(self.progressbar.set_text, text)

    def close(self):
        """Close the loading window.

        This should be called when the workthread has finished it's work.
        This can be called outside the Gtk main thread.
        """
        self.workthread = None
        Gtk.main_quit()

    def cancel(self, widget=None):
        """Close the loading window.

        This should be called when the workthread has finished it's work.
        This can be called outside the Gtk main thread.
        """
        if self.workthread is not None:
            self.workthread.cancel()
        self.close()
