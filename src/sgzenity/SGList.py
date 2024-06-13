import gi

gi.require_version('Gtk', '3.0')
from gi.repository import GLib, GObject, Gtk

from .base import Base


class SGList(Base):
    def __init__(self, columns, items, print_columns, text, *args, **kwargs):
        super(SGList, self).__init__(*args, **kwargs)
        self.columns = columns
        self.items = items
        self.print_columns = print_columns
        self.text = text
        self.selection = None
        self.dialog = Gtk.Dialog()
        self.init_dialog()

    def init_dialog(self):
        super(SGList, self).init_dialog()
        len_col = len(self.columns)
        coltypes = [str] * len_col
        store = Gtk.ListStore(*coltypes)

        # Zenity's Example is filling the cells row by row
        # (https://help.gnome.org/users/zenity/stable/list.html.en)
        # To imitate this we probably need a helper to flatten the items
        # example: [1,2,3,4,5] -> (1,2,3), (4,5,'')
        def group(items, nb_cols):
            for i in range(0, len(items), nb_cols):
                group = items[i : i + nb_cols]
                if len(group) == nb_cols:
                    yield (tuple(group))
                else:
                    # fill empty indices with empty string
                    yield (tuple(group + [''] * (nb_cols - len(group))))

        for g in group(self.items, len_col):
            store.append(g)

        cell = Gtk.CellRendererText()
        treeview = Gtk.TreeView(store)
        treeview.set_border_width(40)
        treeview.show()
        treeview.get_selection().connect("changed", self._on_item_selected)

        for i, column in enumerate(self.columns):
            tvcolumn = Gtk.TreeViewColumn(column)
            tvcolumn.set_sort_column_id(0)
            tvcolumn.pack_start(cell, True)
            tvcolumn.add_attribute(cell, 'text', i)
            treeview.append_column(tvcolumn)

        hb = Gtk.HBox()
        hb.show()
        frame = Gtk.Frame()
        if self.text:
            label = Gtk.Label()
            label.set_text(self.text)
            label.show()
            frame.set_label(self.text)
        frame.show()
        scrolledwindow = Gtk.ScrolledWindow(expand=True)
        scrolledwindow.show()
        scrolledwindow.add(treeview)
        frame.add(scrolledwindow)
        hb.pack_start(frame, True, True, 10)
        vb = self.dialog.get_content_area()
        vb.set_spacing(10)
        vb.add(hb)
        self.dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK
        )
        self.dialog.set_default(
            self.dialog.get_widget_for_response(Gtk.ResponseType.OK)
        )

    def _on_item_selected(self, selection):
        model, treeiter = selection.get_selected()
        if not treeiter:
            self.selection = None
            return
        if self.print_columns is None:
            self.selection = [x for x in model[treeiter]]
        else:
            try:
                self.selection = [model[treeiter][self.print_columns]]
            except IndexError:
                print("Error: Column index out of range")
            except TypeError:
                print("Error: Column index must be integer")

    def set_response(self, response):
        if response == Gtk.ResponseType.OK:
            self.response = self.selection
