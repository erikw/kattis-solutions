#!/usr/bin/env python

n = int(raw_input())
busses = [int(n) for n in raw_input().split()]
busses.sort()

i = 0
while i < len(busses):
    cb = busses[i]
    j = 1
    while i + 1 < len(busses) and busses[i] + 1 == busses[i + 1]:
        j += 1
        i += 1

    if j > 2:
        print "%d-%d" % (cb, busses[i]),
    else:
        for l in range(i - j + 1, i + 1):
            print "%d" % busses[l],
    i += 1
