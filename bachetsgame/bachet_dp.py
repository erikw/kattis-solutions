#!/usr/bin/env python

import sys


# P = False
# N = True

depth=0

def compute_win(n, nbrs, wins):
    global depth
    depth += 1
    print "depth = %d, n = %d" % (depth, n)
    if n == 0:
        wins[n] = False
        return
    for nbr in reversed(nbrs):
        next_n = n - nbr
        if (next_n < 0):
            continue

        if wins[next_n] is None:
            compute_win(next_n, nbrs, wins)
        if wins[next_n]:
            wins[n] = False
        else:
            wins[n] = True
            return

for line in sys.stdin:
    nbrs = [int(x) for x in line.split()]
    n = nbrs.pop(0)
    m = nbrs.pop(0)
    wins = [None] * (n + 1)

    compute_win(n, nbrs, wins)
    if wins[n]:
        print "Stan wins"
    else:
        print "Ollie wins"
