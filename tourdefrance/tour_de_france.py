#!/usr/bin/env python

t = raw_input()
while t != "0":
    front = [int(i) for i in raw_input().split()]
    rear  = [int(i) for i in raw_input().split()]
    ratios = list()
    for f in front:
        for r in rear:
            ratios.append(float(r) / f)
    ratios.sort()

    i = 0
    max_spread = 0
    while i < len(ratios) - 1:
        s = ratios[i + 1] / ratios[i]
        if s > max_spread:
            max_spread = s
        i += 1
    print "%.2f" % max_spread
    t = raw_input()
