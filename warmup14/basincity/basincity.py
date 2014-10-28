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
def r0(graph):
    global rec_cnt
    rec_cnt += 1

    if not graph:
        return 0                # 1
    u = None                    # v w/ most neigh.
    for v, neighbours in graph.iteritems():
        if not neighbours:
            ch = remove_vertex(graph, v)
            tmp = 1 + r0(graph)   # 2
            reinsert(graph, ch)
            return tmp

        if not u or len(neighbours) > len(graph[u]):
            u = v

    # 3
    changed_nodes = []
    neighbours = set(graph[u])
    changed_nodes.append(remove_vertex(graph, u))
    if len(neighbours) >= 2:
        combs = [x for x in itertools.combinations(neighbours, 2)]
        random.shuffle(combs)
        bvals = []
        for comb in combs:
            changed_nodes.append(remove_vertex(graph, comb[0]))
            changed_nodes.append(remove_vertex(graph, comb[1]))
            bvals.append(2 + r0(graph))
            for c in reversed(changed_nodes):
                reinsert(graph, c)
        bval = max(bvals)
        changed_nodes = []
        changed_nodes.append(remove_vertex(graph, u))
    else:
        bval = r0(graph)



    for v in neighbours:
        changed_nodes.append(remove_vertex(graph, v))
    aval = 1 + r0(graph)
    for c in reversed(changed_nodes):
        reinsert(graph, c)

    return max(aval, bval)



intersections = {}
for i, line in enumerate(sys.stdin):
    line = line.split()
    neighbours = set(int(x) - 1 for x in line[1:])
    intersections[i] = neighbours

mis = r0(intersections)

print "mis = %d\nk= %d" % (mis, k)
if mis < k:
    print "impossible"
else:
    print "possible"

sys.exit(0)
