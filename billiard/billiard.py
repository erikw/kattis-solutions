#!/usr/bin/env python

from math import *

a = -1
b = -1
s = -1
m = -1
n = -1

while True:
    a, b, s, m, n = (int(i) for i in raw_input().split())

    if (a == 0 and b == 0 and s == 0 and m == 0 and n == 0):
        break

    hl = a*m
    vl = b*n
    c  = sqrt(hl*hl + vl*vl)
    angle = degrees(acos(hl/c))
    print "%2.2f %2.2f" % (angle, c/s)
