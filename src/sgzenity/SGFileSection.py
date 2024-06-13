import gi

gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk

from .base import Base


class SGFileSelection(Base):
    def __init__(
        self, multiple, directory, save, confirm_overwrite, filename, *args, **kwargs
    ):
        super(SGFileSelection, self).__init__(*args, **kwargs)
        self.multiple = multiple
        self.directory = directory
        self.save = save
        self.confirm_overwrite = confirm_overwrite
        self.filename = filename
        self.dialog = Gtk.FileChooserDialog(
            buttons=(
                Gtk.STOCK_CANCEL,
                Gtk.ResponseType.CANCEL,
                Gtk.STOCK_OK,
                Gtk.ResponseType.OK,
            )
        )
        self.init_dialog()

    def init_dialog(self):
        super(SGFileSelection, self).init_dialog()
        if not self.save and self.multiple:
            self.dialog.set_select_multiple(True)
        if self.directory:
            self.dialog.set_action(Gtk.FileChooserAction.SELECT_FOLDER)
        if self.save:
            self.dialog.set_action(Gtk.FileChooserAction.SAVE)
        if self.confirm_overwrite:
            self.dialog.set_do_overwrite_confirmation(True)
        if self.filename:
            self.dialog.set_filename(self.filename)

    def set_response(self, response):
        if response == Gtk.ResponseType.OK:
            if self.multiple:
                self.response = self.dialog.get_filenames()
            else:
                self.response = self.dialog.get_filename()
