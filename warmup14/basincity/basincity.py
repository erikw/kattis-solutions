#!/usr/bin/env python
import sys, itertools, random

def are_neighbours(comb, intersections):
    for c0 in comb:
        for c1 in comb:
            if c0 in intersections[c1]:
                return True
    return False

def are_neighbours_fast0(comb, intersections):
    while comb:
        c0 = comb.pop()
        for c1 in comb:
            if c0 in intersections[c1]:
                return True
    return False

def are_neighbours_fast1(comb, intersections):
    for i,c0 in enumerate(comb):
        for c1 in comb[i+1:]:
            if c0 in intersections[c1]:
                return True
    return False

k = int(raw_input())
n = int(raw_input())

intersections = []
for line in sys.stdin:
    line = line.split()
    neighbours = set(int(x) - 1 for x in line[1:])
    intersections.append(neighbours)

r = range(0, n)
random.shuffle(r)
combs = itertools.combinations(r, k)
#for c in combs:
    #print c

if all(are_neighbours_fast1(c, intersections) for c in combs):
    print "impossible"
else:
    print "possible"

sys.exit(0)
