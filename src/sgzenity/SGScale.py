import gi

gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk

from .base import Base


class SGScale(Base):
    def __init__(self, text, value, min, max, step, draw_value, *args, **kwargs):
        super(SGScale, self).__init__(*args, **kwargs)
        self.text = text
        adjustment = Gtk.Adjustment(value, min, max, step, 0, 0)
        self.scale = Gtk.Scale(
            orientation=Gtk.Orientation.HORIZONTAL, adjustment=adjustment
        )
        self.scale.set_draw_value(draw_value)
        self.dialog = Gtk.Dialog()
        self.init_dialog()

    def init_dialog(self):
        super(SGScale, self).init_dialog()
        vb = Gtk.VBox()
        vb.show()
        hb = Gtk.HBox()
        hb.show()

        if self.text:
            # justify label on the left
            halign = Gtk.Alignment(xalign=0, yalign=1, xscale=0, yscale=0)
            halign.show()
            text_info = Gtk.Label(self.text)
            text_info.show()
            text_info.set_justify(Gtk.Justification.LEFT)
            halign.add(text_info)
            hb.pack_start(halign, True, True, 10)
            vb.pack_start(hb, True, True, 10)

        # scale settings
        self.scale.show()
        self.scale.set_digits(0)
        vb.add(self.scale)

        self.dialog.get_content_area().add(vb)
        self.dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OK,
            Gtk.ResponseType.OK,
        )
        self.dialog.set_default(
            self.dialog.get_widget_for_response(Gtk.ResponseType.OK)
        )

    def set_response(self, response):
        if response == Gtk.ResponseType.OK:
            self.response = self.scale.get_adjustment().get_value()
