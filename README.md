https://badge.fury.io/py/sgzenity.png
http://badge.fury.io/py/sgzenity

.. image:: https://readthedocs.org/projects/sgzenity/badge/?version=latest
:target: http://sgzenity.readthedocs.io/en/latest/?badge=latest
:alt: Documentation Status

# SGZenity

SGZenity is a library for python which was inspired by Zenity.

When you write scripts, you can use SGZenity to create simple dialogs that interact graphically with the user.

## Requirements

* Python 3
* [GTK+4](https://docs.gtk.org/)
* python3-gi

## Installation

Install using pip :

```bash
$ pip install sgzenity
```

Or clone the repo:

```bash
$ git clone https://github.com/SoftGeekRo/sgzenity.git
$ cd ./sgzenity
$ python setup.py install
```

## Example

Simple dialog:

```python
from src.sgzenity import calendar

result = calendar(title="Awesome Calendar", text="Your birthday ?")
print(result)
```
This code show a calendar dialog :

.. image:: docs/images/screen.png
:align: center

And display the result :

```bash
$ python test.py
$ (year=2017, month=6, day=4)
```

## API

```python
sgzenity.sgzenity.message(title='', text='', width=330, height=120, timeout=None)
```

Display a simple message

Parameters:

* **text** (*str*) – text inside the window

      * **title** (*str*) – title of the window

      * **width** (*int*) – window width

      * **height** (*int*) – window height

      * **timeout** (*int*) – close the window after n seconds

```python
sgzenity.sgzenity.error(title='', text='', width=330, height=120, timeout=None)
```

Display a simple error

Parameters:

* **text** (*str*) – text inside the window

      * **title** (*str*) – title of the window

      * **width** (*int*) – window width

      * **height** (*int*) – window height

      * **timeout** (*int*) – close the window after n seconds

```python
sgzenity.sgzenity.warning(title='', text='', width=330, height=120, timeout=None)
```

Display a simple warning

Parameters:

* **text** (*str*) – text inside the window

      * **title** (*str*) – title of the window

      * **width** (*int*) – window width

      * **height** (*int*) – window height

      * **timeout** (*int*) – close the window after n seconds

```python
sgzenity.sgzenity.question(title='', text='', width=330, height=120, timeout=None)
```

Display a question, possible answer are yes/no.

Parameters:

* **text** (*str*) – text inside the window

      * **title** (*str*) – title of the window

      * **width** (*int*) – window width

      * **height** (*int*) – window height

      * **timeout** (*int*) – close the window after n seconds

Returns:
The answer as a boolean

Return type:
bool

```python
sgzenity.sgzenity.entry(text='', placeholder='', title='', width=330, height=120, timeout=None)
```

Display a text input

Parameters:

* **text** (*str*) – text inside the window

      * **placeholder** (*str*) – placeholder for the input

      * **title** (*str*) – title of the window

      * **width** (*int*) – window width

      * **height** (*int*) – window height

      * **timeout** (*int*) – close the window after n seconds

Returns:
The content of the text input

Return type:
str

```python
sgzenity.sgzenity.password(text='', placeholder='', title='', width=330, height=120, timeout=None)
```

Display a text input with hidden characters

Parameters:

* **text** (*str*) – text inside the window

      * **placeholder** (*str*) – placeholder for the input

      * **title** (*str*) – title of the window

      * **width** (*int*) – window width

      * **height** (*int*) – window height

      * **timeout** (*int*) – close the window after n seconds

Returns:
The content of the text input

Return type:
str

```python
sgzenity.sgzenity.zlist(columns, items, print_columns=None, text='', title='', width=330, height=120, timeout=None)
```
Display a list of values

Parameters:

* **columns** (*list of strings*) – a list of columns name

      * **items** (*list of strings*) – a list of values

      * **print_columns** (*int** (**None if all the columns**)*) –
        index of a column (return just the values from this column)

      * **text** (*str*) – text inside the window

      * **title** (*str*) – title of the window

      * **width** (*int*) – window width

      * **height** (*int*) – window height

      * **timeout** (*int*) – close the window after n seconds

Returns:
A row of values from the table

Return type:
list

```python
sgzenity.sgzenity.file_selection(multiple=False, directory=False, save=False, confirm_overwrite=False, filename=None, title='', width=330, height=120, timeout=None)
```
Open a file selection window

Parameters:

* **multiple** (*bool*) – allow multiple file selection

      * **directory** (*bool*) – only directory selection

      * **save** (*bool*) – save mode

      * **confirm_overwrite** (*bool*) – confirm when a file is
        overwritten

      * **filename** (*str*) – placeholder for the filename

      * **text** (*str*) – text inside the window

      * **title** (*str*) – title of the window

      * **width** (*int*) – window width

      * **height** (*int*) – window height

      * **timeout** (*int*) – close the window after n seconds

Returns:
path of files selected.

Return type:
string or list if multiple enabled

```python
sgzenity.sgzenity.calendar(text='', day=None, month=None, title='', width=330, height=120, timeout=None)
```

Display a calendar

Parameters:

* **text** (*str*) – text inside the window

      * **day** (*int*) – default day

      * **month** (*int*) – default month

      * **text** – text inside the window

      * **title** (*str*) – title of the window

      * **width** (*int*) – window width

      * **height** (*int*) – window height

      * **timeout** (*int*) – close the window after n seconds

Returns:
(year, month, day)

Return type:
tuple

```python
sgzenity.sgzenity.color_selection(show_palette=False, opacity_control=False, title='', width=330, height=120, timeout=None)
```

Display a color selection dialog

Parameters:

* **show_palette** (*bool*) – hide/show the palette with
  preselected colors

      * **opacity_control** (*bool*) – allow to control opacity

      * **title** (*str*) – title of the window

      * **width** (*int*) – window width

      * **height** (*int*) – window height

      * **timeout** (*int*) – close the window after n seconds

Returns:
the color selected by the user

Return type:
str

```python
sgzenity.sgzenity.scale(text='', value=0, min=0, max=100, step=1, draw_value=True, title='', width=330, height=120, timeout=None)
```

Select a number with a range widget

Parameters:

* **text** (*str*) – text inside window

      * **value** (*int*) – current value

      * **min** (*int*) – minimum value

      * **max** (*int*) – maximum value

      * **step** (*int*) – incrementation value

      * **draw_value** (*bool*) – hide/show cursor value

      * **title** (*str*) – title of the window

      * **width** (*int*) – window width

      * **height** (*int*) – window height

      * **timeout** (*int*) – close the window after n seconds

Returns:
The value selected by the user

Return type:
float
