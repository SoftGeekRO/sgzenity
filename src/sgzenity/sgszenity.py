#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from .base import DEFAULT_HEIGHT, DEFAULT_WIDTH, ZLIST_HEIGHT, GObject, Gtk
from .SGCalendar import SGCalendar
from .SGColorSelection import SGColorSelection
from .SGEntryMessage import SGEntryMessage
from .SGEntryPassword import SGEntryPassword
from .SGFileSection import SGFileSelection
from .SGList import SGList
from .SGProgresBar import ProgressBar
from .SGScale import SGScale
from .simpleDialog import SGSimpleDialog


def _simple_dialog(dialog_type, text, title, width, height, timeout):
    dialog = SGSimpleDialog(dialog_type, text, title, width, height, timeout)
    dialog.run()
    return dialog.response


def message(
    title="", text="", width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, timeout=None
):
    """Display a simple message
    :param text: text inside the window
    :type text: str
    :param title: title of the window
    :type title: str
    :param width: window width
    :type width: int
    :param height: window height
    :type height: int
    :param timeout: close the window after n seconds
    :type timeout: int
    """
    return _simple_dialog(Gtk.MessageType.INFO, text, title, width, height, timeout)


def error(title="", text="", width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, timeout=None):
    """Display a simple error

    :param text: text inside the window
    :type text: str
    :param title: title of the window
    :type title: str
    :param width: window width
    :type width: int
    :param height: window height
    :type height: int
    :param timeout: close the window after n seconds
    :type timeout: int
    """
    return _simple_dialog(Gtk.MessageType.ERROR, text, title, width, height, timeout)


def warning(
    title="", text="", width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, timeout=None
):
    """Display a simple warning

    :param text: text inside the window
    :type text: str
    :param title: title of the window
    :type title: str
    :param width: window width
    :type width: int
    :param height: window height
    :type height: int
    :param timeout: close the window after n seconds
    :type timeout: int
    """
    return _simple_dialog(Gtk.MessageType.WARNING, text, title, width, height, timeout)


def question(
    title="", text="", width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, timeout=None
):
    """Display a question, possible answer are yes/no.

    :param text: text inside the window
    :type text: str
    :param title: title of the window
    :type title: str
    :param width: window width
    :type width: int
    :param height: window height
    :type height: int
    :param timeout: close the window after n seconds
    :type timeout: int
    :return: The answer as a boolean
    :rtype: bool
    """
    response = _simple_dialog(
        Gtk.MessageType.QUESTION, text, title, width, height, timeout
    )
    if response == Gtk.ResponseType.YES:
        return True
    elif response == Gtk.ResponseType.NO:
        return False
    return None


def entry(
    text="",
    placeholder="",
    title="",
    width=DEFAULT_WIDTH,
    height=DEFAULT_HEIGHT,
    timeout=None,
):
    """Display a text input

    :param text: text inside the window
    :type text: str
    :param placeholder: placeholder for the input
    :type placeholder: str
    :param title: title of the window
    :type title: str
    :param width: window width
    :type width: int
    :param height: window height
    :type height: int
    :param timeout: close the window after n seconds
    :type timeout: int
    :return: The content of the text input
    :rtype: str
    """
    dialog = SGEntryMessage(text, placeholder, title, width, height, timeout)
    dialog.run()
    return dialog.response


def password(
    text="",
    placeholder="",
    title="",
    width=DEFAULT_WIDTH,
    height=DEFAULT_HEIGHT,
    timeout=None,
):
    """Display a text input with hidden characters

    :param text: text inside the window
    :type text: str
    :param placeholder: placeholder for the input
    :type placeholder: str
    :param title: title of the window
    :type title: str
    :param width: window width
    :type width: int
    :param height: window height
    :type height: int
    :param timeout: close the window after n seconds
    :type timeout: int
    :return: The content of the text input
    :rtype: str
    """
    dialog = SGEntryPassword(text, placeholder, title, width, height, timeout)
    dialog.run()
    return dialog.response


def sglist(
    columns,
    items,
    print_columns=None,
    text="",
    title="",
    width=DEFAULT_WIDTH,
    height=ZLIST_HEIGHT,
    timeout=None,
):
    """Display a list of values

    :param columns: a list of columns name
    :type columns: list of strings
    :param items: a list of values
    :type items: list of strings
    :param print_columns: index of a column (return just the values from this column)
    :type print_columns: int (None if all the columns)
    :param text: text inside the window
    :type text: str
    :param title: title of the window
    :type title: str
    :param width: window width
    :type width: int
    :param height: window height
    :type height: int
    :param timeout: close the window after n seconds
    :type timeout: int
    :return: A row of values from the table
    :rtype: list
    """
    dialog = SGList(columns, items, print_columns, text, title, width, height, timeout)
    dialog.run()
    return dialog.response


def file_selection(
    multiple=False,
    directory=False,
    save=False,
    confirm_overwrite=False,
    filename=None,
    title="",
    width=DEFAULT_WIDTH,
    height=DEFAULT_HEIGHT,
    timeout=None,
):
    """Open a file selection window

    :param multiple: allow multiple file selection
    :type multiple: bool
    :param directory: only directory selection
    :type directory: bool
    :param save: save mode
    :type save: bool
    :param confirm_overwrite: confirm when a file is overwritten
    :type confirm_overwrite: bool
    :param filename: placeholder for the filename
    :type filename: str
    :param text: text inside the window
    :type text: str
    :param title: title of the window
    :type title: str
    :param width: window width
    :type width: int
    :param height: window height
    :type height: int
    :param timeout: close the window after n seconds
    :type timeout: int
    :return: path of files selected.
    :rtype: string or list if multiple enabled
    """
    dialog = SGFileSelection(
        multiple,
        directory,
        save,
        confirm_overwrite,
        filename,
        title,
        width,
        height,
        timeout,
    )
    dialog.run()
    return dialog.response


def calendar(
    text="",
    day=None,
    month=None,
    year=None,
    title="",
    width=DEFAULT_WIDTH,
    height=DEFAULT_HEIGHT,
    timeout=None,
):
    """Display a calendar

    :param text: text inside the window
    :type text: str
    :param day: default day
    :type day: int
    :param month: default month
    :type month: int
    :param text: text inside the window
    :type text: str
    :param title: title of the window
    :type title: str
    :param width: window width
    :type width: int
    :param height: window height
    :type height: int
    :param timeout: close the window after n seconds
    :type timeout: int
    :return: (year, month, day)
    :rtype: tuple
    """
    dialog = SGCalendar(text, day, month, year, title, width, height, timeout)
    dialog.run()
    return dialog.response


def color_selection(
    show_palette=False,
    opacity_control=False,
    title="",
    width=DEFAULT_WIDTH,
    height=DEFAULT_HEIGHT,
    timeout=None,
):
    """Display a color selection dialog

    :param show_palette: hide/show the palette with preselected colors
    :type show_palette: bool
    :param opacity_control: allow to control opacity
    :type opacity_control: bool
    :param title: title of the window
    :type title: str
    :param width: window width
    :type width: int
    :param height: window height
    :type height: int
    :param timeout: close the window after n seconds
    :type timeout: int
    :return: the color selected by the user
    :rtype: str
    """
    dialog = SGColorSelection(
        show_palette, opacity_control, title, width, height, timeout
    )
    dialog.run()
    return dialog.response


def scale(
    text="",
    value=0,
    min=0,
    max=100,
    step=1,
    draw_value=True,
    title="",
    width=DEFAULT_WIDTH,
    height=DEFAULT_HEIGHT,
    timeout=None,
):
    """Select a number with a range widget

    :param text: text inside window
    :type text: str
    :param value: current value
    :type value: int
    :param min: minimum value
    :type min: int
    :param max: maximum value
    :type max: int
    :param step: incrementation value
    :type step: int
    :param draw_value: hide/show cursor value
    :type draw_value: bool
    :param title: title of the window
    :type title: str
    :param width: window width
    :type width: int
    :param height: window height
    :type height: int
    :param timeout: close the window after n seconds
    :type timeout: int
    :return: The value selected by the user
    :rtype: float
    """
    dialog = SGScale(
        text, value, min, max, step, draw_value, title, width, height, timeout
    )
    dialog.run()
    return dialog.response
