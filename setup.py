#!/usr/bin/env python

from distutils.core import setup

setup(
    name='unicode-text-style',
    version='0.1',
    description='Python Unicode combining characters styler',
    author='Kelvin Santos',
    author_email='kelvinsteinersantos@gmail.com',
    url='https://github.com/kelvinss',
    py_modules = ['unicode_text_style'],
    scripts = ['text-style'],
    extras_require = {
        'clipboard':  ['pyperclip'],
    }
)
