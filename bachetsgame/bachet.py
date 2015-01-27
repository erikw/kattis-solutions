#!/usr/bin/env python

import sys


def can_win(i, nbrs, wins):
    for nbr in nbrs:
        if nbr <= i:
            if not wins[i - nbr]:
                return True
    return False


for line in sys.stdin:
    nbrs = [int(x) for x in line.split()]
    n = nbrs.pop(0)
    m = nbrs.pop(0)
    wins = [False] * (n + 1)
    for i in xrange(1, len(wins)):
        wins[i] = can_win(i, nbrs, wins)
    if wins[n]:
        print "Stan wins"
    else:
        print "Ollie wins"
