#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A single if statement."""

MYINPUT = raw_input('Tell me a story! ')
MAX_LENGTH = 80
LONGSTR = 'short'

INPUT_LENGTH = len(MYINPUT)

if INPUT_LENGTH > MAX_LENGTH:
    LONGSTR = 'long'
else:
    LONGSTR = 'short'

OUTPUT = 'That certainly was a {} story!'.format(LONGSTR)
print OUTPUT
