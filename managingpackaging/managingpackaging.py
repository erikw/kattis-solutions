#!/usr/bin/env python

import sys
from collections import defaultdict
from pprint import pprint


def tarjan(G):
    """Implementation of Tarjan's topologial sorting algorithm.


    Unfortunately wasted since it can't break ties lexicographically which is
    necessary in this task. Implementation left for educational purposes.
    """
    temp_marked = set()
    perm_marked = set()
    L = list()

    keys = list(sorted(G, reverse=True))

    def visit(n):
        if n in temp_marked:
            return False
        if n not in perm_marked:
            temp_marked.add(n)
            for v in sorted(G[n]):
                if not visit(v):
                    return False
            perm_marked.add(n)
            temp_marked.remove(n)
            L.append(n)
        return True

    while keys:
        if not visit(keys.pop()):
            return None

    return L


def kahn(G, rG):
    """Implementation of Kahn's topological sorting algorithm.

    Orders the given graph lexicographically.
    """
    L = list()
    S = set()

    for k,v in G.items():
        if not v:
            S.add(k)
    if not S:
        return None
    S = list(sorted(S, reverse=True))

    while S:
        n = S.pop()
        L.append(n)
        for m in rG[n].copy():
            G[m].remove(n)
            if not G[m]:
                S.append(m)
        S.sort(reverse=True)

    for k,v in G.items():
        if v:
            return []
    return L



def main():
    n = int(raw_input())
    while True:
        deps = defaultdict(set)
        rdeps = defaultdict(set)
        for _ in range(n):
            line = raw_input().split()
            deps[line[0]].update(line[1:])
            rdeps[line[0]]
            for dep in line[1:]:
                rdeps[dep].add(line[0])
        ordering = kahn(deps, rdeps)
        if ordering:
            for item in ordering:
                print item
        else:
            print "cannot be ordered"
        n = int(raw_input())
        if n == 0:
            break
        print

    return 0

if __name__ == '__main__':
    sys.exit(main())
