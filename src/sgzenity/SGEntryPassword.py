import gi

gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk

from .SGEntry import SGEntry


class SGEntryPassword(SGEntry):
    def __init__(self, *args, **kwargs):
        super(SGEntryPassword, self).__init__(*args, **kwargs)

    def init_dialog(self):
        super(SGEntryPassword, self).init_dialog()
        hb_up = Gtk.HBox(spacing=20)
        hb_up.show_all()

        # Password icon
        icon = Gtk.Image()
        icon.set_from_stock(Gtk.STOCK_DIALOG_AUTHENTICATION, Gtk.IconSize.DIALOG)
        icon.show()
        hb_up.add(icon)
        # Text display on the dialog
        if self.text:
            text_label = Gtk.Label()
            text_label.set_text(self.text)
            text_label.show()
            hb_up.add(text_label)
        self.dialog.get_content_area().add(hb_up)

        hb_down = Gtk.HBox(spacing=20)
        hb_down.show_all()

        hb_down.add(self.entry_widget)
        self.dialog.get_content_area().add(hb_down)
        self.entry_widget.set_visibility(False)
