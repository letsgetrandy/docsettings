#! /usr/bin/python

import os
import re
import sys


class DocSettings(object):
    settings = {}

    def __init__(self, module):
        if os.path.isdir(module):
            for filename in os.listdir(module):
                self.process(os.path.join(module, filename))
        else:
            self.process(module)
        for (setting, comment) in self.settings.items():
            print '%s%s\n' % (comment, setting)
        #print self.settings

    def process(self, filename):
        comment = []
        setting = ''
        has_setting = re.compile(r'^\s*\b(\w+)\b\s*=')
        for line in open(filename):
            m = re.match(has_setting, line)
            if line.startswith('#'):
                comment.append(line)
            elif m:
                setting = m.group(1)
                if comment:
                    self.settings[setting] = ''.join(comment)
            else:
                comment = []
                setting = ''


DocSettings(sys.argv[1])
