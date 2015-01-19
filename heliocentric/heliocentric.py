#!/usr/bin/env python

import sys

# There should be a way smarter way to solve this...
for i, line in enumerate(sys.stdin, 1):
    e, m = (int(i) for i in line.split())
    days = 0
    while e % 365 != 0 or m % 687 != 0:
        e += 1
        m += 1
        days += 1
    print "Case %d: %d" % (i, days)
