#!/usr/bin/env python

import sys
from math import *

class Node(object):

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.neighbors = list()
        
    def __hash__(self):
        return hash((x, y, r))

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

    
def add_crane(G, n):
    for other in G:
        pass


def weighted_independent_set(G):
    pass


def main():
    ncases = int(raw_input())
    for i in range(ncases):
        cranes = int(raw_input())
        G = set()
        for j in range(cranes):
            x, y, r = (int(k) for k in raw_input().split())
            add_crane(G, Node(x, y, r))
        A = weighted_independent_set(G)
            
if __name__ == '__main__':
    test_intersects()
    main()




