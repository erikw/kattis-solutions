#!/usr/bin/env python
import sys, itertools, random


k = int(raw_input())
n = int(raw_input())


def remove_vertex(g, v):
    removed = (v, g[v])
    for u in g[v]:
        g[u].remove(v)
    del g[v]
    return removed

def reinsert(g, ch):
    # ch = removed above
    g[ch[0]] = ch[1]
    for u in ch[1]:
        g[u].add(ch[0])

rec_cnt = 0
def r0(g):
    global rec_cnt
    rec_cnt += 1

    if not g:
        return 0                # 1
    u = None                    # v w/ most neigh.
    for v, n in g.iteritems():
        if not n:
            ch = remove_vertex(g, v)
            tmp = 1 + r0(g)   # 2
            reinsert(g, ch)
            return tmp

        if not u or len(n) > len(g[u]):
            u = v

    # 3
    ch = []
    nb = set(g[u])
    ch.append(remove_vertex(g, u))
    bval = r0(g)
    for v in nb:
        ch.append(remove_vertex(g, v))
    aval = 1 + r0(g)
    for c in reversed(ch):
        reinsert(g, c)

    return max(aval, bval)



intersections = {}
for i, line in enumerate(sys.stdin):
    line = line.split()
    neighbours = set(int(x) - 1 for x in line[1:])
    intersections[i] = neighbours

mis = r0(intersections)

if mis < k:
    print "impossible"
else:
    print "possible"

sys.exit(0)
