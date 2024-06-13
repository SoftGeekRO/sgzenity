import gi

gi.require_version('Gtk', '3.0')
from gi.repository import GLib, GObject, Gtk

DEFAULT_WIDTH = 330
DEFAULT_HEIGHT = 120
ZLIST_HEIGHT = 400


class Base(Gtk.Window):
    def __init__(
        self,
        title="Title",
        width=DEFAULT_WIDTH,
        height=DEFAULT_HEIGHT,
        timeout=None,
        *args,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.title = title
        self.width = width
        self.height = height
        self.timeout = timeout

        self.dialog = None
        self.response = None

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.vbox)

    def init_dialog(self):
        # global config
        self.dialog.set_resizable(True)
        self.dialog.resize(self.width, self.height)
        self.dialog.set_border_width(10)
        if self.timeout:
            GLib.timeout_add_seconds(self.timeout, self._destroy, self.dialog)

        if self.title:
            self.dialog.set_title(self.title)

        self.connect('delete_event', self.delete_event)
        # Connect the destroy event so that we can set the done flag and
        # terminate the worker cleanly.
        self.dialog.connect("destroy", self._destroy)

    def _destroy(self, widget=None):
        """Quit the application

        Handler called when the application is about to quit.

        Set the done flag so that the worker quits cleanly, then quit.

        :param widget:
        :return:
        """
        Gtk.main_quit()

    def run(self):
        self.dialog.show()
        self.dialog.connect("response", self._response)
        Gtk.main()

    def _response(self, dialog, response):
        self.set_response(response)
        self._destroy(self.dialog)

    def delete_event(self, *args):
        return False

    def set_response(self, response):
        self.response = response
