import gi

gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk

from .SGEntry import SGEntry


class SGEntryMessage(SGEntry):
    def __init__(self, *args, **kwargs):
        super(SGEntryMessage, self).__init__(*args, **kwargs)

    def init_dialog(self):
        super(SGEntryMessage, self).init_dialog()
        # Display text on the dialog before the input
        if self.text:
            text_label = Gtk.Label()
            text_label.set_text(self.text)
            text_label.show()
            self.dialog.get_content_area().add(text_label)
        self.dialog.get_content_area().add(self.entry_widget)
