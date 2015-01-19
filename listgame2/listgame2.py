#!/usr/bin/env python

import sys
from math import sqrt

n = num = int(raw_input())
facts = 0
divs = list()

for i in xrange(2, int(sqrt(num)) + 1):
    if num % i == 0:
        divs.append(i)
        facts += 1
        num //= i
    if divs and num < divs[-1]:
        break

#TODO, but WHAT?
wrong=False
if not divs or (num > 1 and num > divs[-1]):
    wrong = num != 1 and num in divs
    facts += 1

print n, divs, num, facts

if wrong:
    sys.exit(1)
