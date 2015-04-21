#!/usr/bin/env python

import sys
from math import *

class Node(object):

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.neighbors = set()
        
    def __hash__(self):
        return hash((self.x, self.y, self.r))

    def __str__(self):
        s = ", ".join(("(% d, % d, % d)" % (n.x, n.y, n.r) for n in self.neighbors))
        return "(% d, % d, % d): %s" % (self.x, self.y, self.r, s) 

    def intersects(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        dr = self.r + other.r
        return dx*dx + dy*dy <= dr*dr
    

def test_intersects():
    n0 = Node(0, 0, 4)
    n1 = Node(5, 0, 4)
    n2 = Node(-4, 0, 4)
    n3 = Node(4, 0, 4)
    assert n0.intersects(n1)
    assert n1.intersects(n0)
    assert not n1.intersects(n2)
    assert n3.intersects(n2)


class Graph(object):

    def __init__(self):
        self.nodes = set()

    def __bool__(self):
        return bool(self.nodes)

    def __nonzero__(self):
        return bool(self.nodes)
        
    def __iter__(self):
        return iter(self.nodes)
        
    def add_crane(self, n):
        for o in self.nodes:
            if n.intersects(o):
                n.neighbors.add(o)
                o.neighbors.add(n)
        self.nodes.add(n)

    def pop_crane(self, n = None):
        if not n:
            n = self.nodes.pop()
        else:
            self.nodes.remove(n)
        for o in n.neighbors:
            o.neighbors.remove(n)
        return n

    def __str__(self):
        lstr = list()
        lstr.append("{")
        for o in self:
            lstr.append(str(o))
        lstr.append("}")
        return "\n".join(lstr)

def weighted_independent_set(G):
    if not G:
        return 0

    # Recurse without n.
    n = G.pop_crane()
    res0 = weighted_independent_set(G)


    # Recurse with n.
    neighs = list(n.neighbors)
    for o in neighs:
        G.pop_crane(o)
    res1 = weighted_independent_set(G) + n.r*n.r

    for o in neighs:
        G.add_crane(o)
    G.add_crane(n)
        
    return max(res0, res1)
    

def main():
    ncases = int(raw_input())
    for i in range(ncases):
        cranes = int(raw_input())
        G = Graph()
        for j in range(cranes):
            x, y, r = (int(k) for k in raw_input().split())
            G.add_crane(Node(x, y, r))

        A = weighted_independent_set(G)
        print A
            
if __name__ == '__main__':
    test_intersects()
    main()




