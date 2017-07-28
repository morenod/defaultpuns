#!/bin/python

import os
import re
import sys


def isValidRegex(regexp=""):
    try:
        re.compile(regexp)
        is_valid = True
    except re.error:
        is_valid = False
    return is_valid

exitcode = 0

for file in os.listdir('./'):
    if not os.path.isdir(file) and not file.startswith('.'):
        with open(os.path.expanduser(file), 'r') as staticpuns:
            number = 0
            for line in staticpuns:
                number += 1
                if not len(line.split('|')) == 2:
                    print "Incorrect number of fields on line %s of file %s." % (str(number), file)
                    exitcode = 2
                elif not isValidRegex(line.split('|')[0]):
                    print "Incorrect regex trigger %s on line %s of file %s." % (line.split('|')[0], str(number), file)
                    exitcode = 2
sys.exit(exitcode)
