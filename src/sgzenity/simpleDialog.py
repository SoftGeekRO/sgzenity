import gi

gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk

from .base import Base


class SGSimpleDialog(Base):
    def __init__(self, dialog_type, text, *args, **kwargs):
        super(SGSimpleDialog, self).__init__(*args, **kwargs)
        self.text = text
        self.dialog_type = dialog_type

        # Buttons
        if self.dialog_type == Gtk.MessageType.QUESTION:
            buttons = Gtk.ButtonsType.YES_NO
        else:
            buttons = Gtk.ButtonsType.OK
        # Dialog
        self.dialog = Gtk.MessageDialog(
            parent=None,
            flags=0,
            type=self.dialog_type,
            buttons=buttons,
            message_format=None,
        )
        self.vbox.pack_start(self.dialog, True, True, 0)

        self.init_dialog()

    def init_dialog(self):
        super(SGSimpleDialog, self).init_dialog()
        if self.text:
            self.dialog.set_markup(self.text)
