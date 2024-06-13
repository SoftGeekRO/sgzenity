import gi

gi.require_version('Gtk', '3.0')
from gi.repository import GLib, GObject, Gtk

from .base import Base


class SGColorSelection(Base):
    def __init__(self, show_palette, opacity_control, *args, **kwargs):
        super(SGColorSelection, self).__init__(*args, **kwargs)
        self.dialog = Gtk.ColorSelectionDialog()
        self.dialog.get_color_selection().set_has_palette(show_palette)
        self.opacity_control = opacity_control
        self.dialog.get_color_selection().set_has_opacity_control(opacity_control)
        self.init_dialog()

    def set_response(self, response):
        if response == Gtk.ResponseType.OK:
            self.response = (
                self.dialog.get_color_selection().get_current_rgba().to_string()
            )
