import gi

gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk

from .base import Base


class SGEntry(Base):
    def __init__(self, text, placeholder, *args, **kwargs):
        super(SGEntry, self).__init__(*args, **kwargs)
        self.text = text
        self.placeholder = placeholder
        # Widget
        self.entry_widget = Gtk.Entry()
        self.entry_widget.show()
        # Focus on the text input
        self.entry_widget.set_activates_default(True)
        # Dialog
        self.dialog = Gtk.Dialog()
        self.init_dialog()

    def init_dialog(self):
        super(SGEntry, self).init_dialog()

        if self.placeholder:
            self.entry_widget.set_text(self.placeholder)

        self.dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK
        )
        self.dialog.set_default(
            self.dialog.get_widget_for_response(Gtk.ResponseType.OK)
        )

    def set_response(self, response):
        if response == Gtk.ResponseType.OK:
            self.response = self.entry_widget.get_text()
