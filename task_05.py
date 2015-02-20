#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Blood Pressure Reading"""

MYINPUT = raw_input('What is your blood pressure? ')
MYINPUT = int(MYINPUT)

if MYINPUT <= 89:
    BP_STATUS = 'Low'
elif MYINPUT > 89 <= 119:
    BP_STATUS = 'Ideal'
elif MYINPUT > 119 <= 139:
    BP_STATUS = 'Warning'
elif MYINPUT > 139 <= 159:
    BP_STATUS = 'High'
else:
    BP_STATUS = 'Emergency'

OUTPUT = 'Your status is currently: {}'.format(BP_STATUS)
print OUTPUT
