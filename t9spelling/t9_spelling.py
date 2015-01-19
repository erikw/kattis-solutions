#!/usr/bin/env python

import sys

t9_kbd = {
    " " : "0",
    "a" : "2",
    "b" : "22",
    "c" : "222",

    "d" : "3",
    "e" : "33",
    "f" : "333",

    "g" : "4",
    "h" : "44",
    "i" : "444",

    "j" : "5",
    "k" : "55",
    "l" : "555",

    "m" : "6",
    "n" : "66",
    "o" : "666",

    "p" : "7",
    "q" : "77",
    "r" : "777",
    "s" : "7777",
    
    "t" : "8",
    "u" : "88",
    "v" : "888",

    "w" : "9",
    "x" : "99",
    "y" : "999",
    "z" : "9999",
    }

n = int(raw_input())
prev = "-"
for i in range(1, n + 1):
    line = raw_input()
    tmp = " "
    for c in line:
        t = t9_kbd[c]
        if t[-1] == prev[-1]:
            tmp += " "
        tmp += t
        prev = tmp
    print "Case #%d:%s" % (i, tmp)




