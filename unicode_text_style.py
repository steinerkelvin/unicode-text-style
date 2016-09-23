#!/usr/bin/env python
# coding: UTF-8

"""Style text using combining Unicode characters.

Examples:

U̲n̲d̲e̲r̲l̲i̲n̲e̲d̲ t̲e̲x̲t̲.

S̶t̶r̶i̶k̶e̶d̶ t̶e̶x̶t̶.

O̅v̅e̅r̅l̅i̅n̅e̅d̅ t̅e̅x̅t̅.
"""

import re

__all__ = ['style_piece', 'style_text', 'CHARS']


_sep_patt = re.compile("(\W+)")

CHAR_OVER = unichr(0x0305)
CHAR_UNDER = unichr(0x0332)
CHAR_STRIKE = unichr(0x0336)

CHARS = {"over": CHAR_OVER, "under": CHAR_UNDER, "strike": CHAR_STRIKE, }


def style_piece(st, char=CHAR_UNDER):
    """Append 'char' after each character of 'st'."""

    # Adds the selected character after each character of the string
    return char.join(list(st)+[""])


def style_text(text, char=CHAR_UNDER, a=False):
    """Append 'char' after each character of each word of 'text'.

    If 'a' is true, append after all characters (including whitespaces)
    """

    if a:
        return style_piece(text, char)
    else:
        splited = _sep_patt.split(text)

        result = []
        for st in splited:
            if not _sep_patt.match(st):
                st = style_piece(st, char)
            result.append(st)

        return "".join(result)

