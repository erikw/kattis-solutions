#!/usr/bin/env python2

import sys

n=int(raw_input())

for i in xrange(1,n+1):
    last=None
    sys.stdout.write("Case #%d: " % i)
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
            sys.stdout.write(" ")
        last = nbr
        sys.stdout.write(str(nbr) * repeat)
    sys.stdout.write('\n')
