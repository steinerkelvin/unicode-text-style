
# unicode-text-style

Simple script that takes a piece of text and styles it using combining Unicode 
characters.

Avaiable styles are: underline, overline and strikethrough.

Examples:

* U̲n̲d̲e̲r̲l̲i̲n̲e̲d̲ t̲e̲x̲t̲.
* S̶t̶r̶i̶k̶e̶d̶ t̶e̶x̶t̶.
* O̅v̅e̅r̅l̅i̅n̅e̅d̅ t̅e̅x̅t̅.


## Install

`# python setup.py install`

To enable copying to clipboard, install the [`pyperclip`](https://pypi.python.org/pypi/paperclip) python package:

`# pip install pyperclip`


## Usage

    text-style [-h] [-a] [-o] [-u] [-s] text
    
    -h, --help    show this help message and exit
    -a, --all     Style all characters (including non-alphanumeric)
    -o, --over    Overline
    -u, --under   Underline
    -s, --strike  Strikethrough
