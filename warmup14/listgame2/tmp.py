#!/usr/bin/env python

import commands
import sys

for i in xrange(1000, 10**15):
    if i % 1000 == 0:
        print i

    (s,o) = commands.getstatusoutput('echo %d | ./listgame2.py' % i)

    if s:
        print o
        sys.exit(s)
