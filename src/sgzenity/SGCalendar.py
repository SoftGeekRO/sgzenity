import gi

gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk

from .base import Base


class SGCalendar(Base):
    def __init__(self, text, day, month, year, *args, **kwargs):
        super(SGCalendar, self).__init__(*args, **kwargs)
        self.text = text
        self.day = day
        self.month = month
        self.year = year
        self.calendar = Gtk.Calendar()
        self.dialog = Gtk.Dialog()
        self.init_dialog()

    def init_dialog(self):
        super(SGCalendar, self).init_dialog()
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

        if self.day:
            self.calendar.set_day = self.day
        if self.month:
            self.calendar.set_month = self.month
        if self.year:
            self.calendar.set_year = self.year

        self.calendar.show()
        self.calendar.connect('day-selected-double-click', self._day_selected, None)
        vb.add(self.calendar)

        self.dialog.get_content_area().add(vb)
        self.dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK
        )
        self.dialog.set_default(
            self.dialog.get_widget_for_response(Gtk.ResponseType.OK)
        )

    def _day_selected(self, calendar, event):
        self.dialog.response(Gtk.ResponseType.OK)

    def set_response(self, response):
        if response == Gtk.ResponseType.OK:
            self.response = self.calendar.get_date()
