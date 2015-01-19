#!/usr/bin/env python

import sys

n, d = (int(i) for i in raw_input().split())
while n != 0 and d != 0:
    print("%d %d / %d" % (n / d, n % d, d))
    n, d = (int(i) for i in raw_input().split())
