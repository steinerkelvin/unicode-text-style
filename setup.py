#!/usr/bin/env python

from distutils.core import setup

setup(
    name='unicode-text-style',
    version='0.2',
    description='Script that styles a piece of text using combining Unicode characters',
    author='Kelvin Santos',
    author_email='kelvinsteinersantos@gmail.com',
    url='https://github.com/kelvinss/unicode-text-style',
    py_modules = ['unicode_text_style'],
    scripts = ['text-style'],
    extras_require = {
        'clipboard':  ['pyperclip'],
    }
)
