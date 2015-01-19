#!/usr/bin/env python
from __future__ import print_function

import sys

n=int(raw_input())

for i in xrange(n):
    last=None
    print("Case #%d: " % (i+1), end="")
    word=raw_input()
    for c in word[:]:
        if c == " ":
            nbr = 0
            repeat = 1
        elif c in "pqrs":
            nbr = 7
            repeat = 1 + ord(c) - ord("p")
        elif c in "tuv":
            nbr = 8
            repeat = 1 + ord(c) - ord("t")
        elif c in "wxyz":
            nbr = 9
            repeat = 1 + ord(c) - ord("w")
        else:
            nbr = (ord(c) - ord("a"))/3 + 2
            repeat = 1 + ord(c) - ((nbr - 2) * 3 + ord("a"))
        if last == nbr:
            print(" ", end="")
        last = nbr
        print(str(nbr) * repeat, end="")
    print("")
