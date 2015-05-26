#!/usr/bin/env python

import sys

from collections import defaultdict
from Queue import PriorityQueue

# TODO: Hur ska past_cost definieras med tanke på tanken?

def A_star(G, start, goal, past_cost, future_cost):
    """Perform A* searching algorithm."""

    def reconstruct_path(came_from, current):
        """Reconstruct the path we took throughout the searching."""
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        return total_path

    def neighbor_nodes(current):
        return [ e.term for e in current.edges ]

    FAILURE = None
    closed_set = set()
    open_set = PriorityQueue()
    in_open = set()

    came_from = dict()
    g_score = dict()
    f_score = dict()

    open_set.put(start)
    in_open.add(start)
    g_score[start] = 0
    f_score[start] = g_score[start] + future_cost(G, start, goal)

    while in_open:
        current = open_set.get()
        in_open.remove(current)
        if current == goal:
            return reconstruct_path(came_from, goal)

        closed_set.add(current)
        for n in neighbor_nodes(current):
            if n in closed_set:
                continue
            # TODO: Remove g_score[current] after test is done.
            tentative_g = g_score[current] + past_cost(current, n)

            if n not in in_open or tentative_g < g_score[n]:
                came_from[n] = current
                g_score[n] = tentative_g
                f_score[n] = g_score[n] + future_cost(G, n, goal)

                if n not in in_open:
                    open_set.put(n)
                    in_open.add(n)

    return FAILURE


def dijkstra(G, source):
    G = { n: DijkstraNode(n) for k,n in G.iteritems() }


class DijkstraNode(object):
    def __init__(self, node, dist=sys.maxint):
        self.node = node
        self.dist = dist

    def __cmp__(self, other):
        return self.dist - self.other

class Node(object):

    def __init__(self, iid):
        self.iid = iid
        self.edges = set()

    def __hash__(self):
        return hash(self.iid)

    def __eq__(self, other):
        return self.iid == other.iid

    def __str__(self):
        return str(self.iid)

    def add_neighbor(self, neighbor, **kw_args):
        self.edges.add(Edge(self, neighbor, **kw_args))
        neighbor.edges.add(Edge(neighbor, self, **kw_args))


class Edge(object):

    def __init__(self, src, term, **kw_args):
        self.src = src
        self.term = term
        self.props = dict(kw_args)

    def __hash__(self):
        return hash(self.src) + hash(self.term)

    def __eq__(self, other):
        return (self.src == other.src and
                self.term == other.term and
                self.props == other.props)

    def __str__(self):
        return str(self.src) + "->" + str(self.term)


nodes = dict()
def get_node(i):
    if not i in nodes:
        print "making new node for ", i
        nodes[i] = Node(i)

    return nodes[i]


def read_input():
    # n = number of cities, m = number of roads
    (n, m) = (int(i) for i in raw_input().split())
    # [] of gas prices in each city
    prices = [int(i) for i in raw_input().split()]

    for _ in range(m):
        # di = distance of road between city ui and vi
        (ui, vi, di) = (int(i) for i in raw_input().split())
        ui = get_node(ui)
        vi = get_node(vi)
        ui.add_neighbor(vi, cost=di)

    # q = number of queries to run
    q = int(raw_input())

    # TODO: Perhaps better data structure for the queries?
    queries = []
    for _ in range(q):
        # ci = fuel capacity of vehicle, si = start city, ei = end city
        (ci, si, ei) = (int(i) for i in raw_input().split())
        si = get_node(si)
        ei = get_node(ei)
        queries.append((ci, si, ei))

    return (n, m, prices, queries)


def main():
    n, m, prices, queries = read_input()

    def future_cost():
        pass
    for (capacity, start, end) in queries:
        def past_cost():
            pass

        path = A_star(nodes, start, end, past_cost, future_cost)
        if path:
            for p in path:
                a = 

        else:
            print "impossible"


def build_graph():
    G = dict()

    def create_and_add_node(_id):
        G[_id] = Node(_id)
        return G[_id]

    s = create_and_add_node("s")
    t = create_and_add_node("t")
    a = create_and_add_node("a")
    b = create_and_add_node("b")
    c = create_and_add_node("c")
    d = create_and_add_node("d")
    e = create_and_add_node("e")

    s.add_neighbor(a, cost=1.5)
    s.add_neighbor(d, cost=2)

    a.add_neighbor(b, cost=2)
    b.add_neighbor(c, cost=3)
    c.add_neighbor(t, cost=4)
    d.add_neighbor(e, cost=3)
    e.add_neighbor(t, cost=2)

    return G


def test_dijkstra():
    G = build_graph()
    source = G["s"]

    # TODO

def test_A_star():
    G = build_graph()
    s = G["s"]
    t = G["t"]

    h = {}
    h[G["a"]] = 4
    h[G["b"]] = 2
    h[G["c"]] = 4
    h[G["d"]] = 4.5
    h[G["e"]] = 2
    h[G["t"]] = 1337

    def past(src, term):
        for e in src.edges:
            if e.term == term:
                return e.props['cost']
        raise RuntimeError("Should never happen")

    def future(_G, src, term):
        print term
        return h[term]

    path = A_star(s, s, t, past, future)
    for p in path:
        print p


if __name__ == '__main__':
    main()
