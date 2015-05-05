#!/usr/bin/env python

from collections import defaultdict
from Queue import PriorityQueue

def A_star(G, start, goal, dist_between, past_cost, future_cost):
    """Perform A* searching algorithm."""

    def reconstruct_path(came_from, current):
        """Reconstruct the path we took throughout the searching."""
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        return total_path

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
        for n in neightbor_nodes(G, current):
            if n in closed_set:
                continue
            tentative_g = g_score[current] + dist_between(current, n)

            if n not in in_open or tentative_g < g_score[n]:
                came_from[n] = current
                g_score[n] = tentative_g
                f_score[n] = g_score[n] + future_cost(G, n, goal)

                if n not in in_open:
                    open_set.put(n)
                    in_open.add(n)

    return FAILURE


class Node(object):

    def __init__(self, iid):
        self.iid = iid
        self.neighbors = set()

    def __hash__(self):
        return hash(iid)

    def __eq__(self, other):
        return self.iid == other.iid

    def __str__(self):
        return str(self.iid)

    def add_neighbor(self, *args):
        for a in args:
            self.neightbor.add(other)


class Edge(object):

    def __init__(self, a, b, **kw_args):
        self.a = a
        self.b = b
        self.props = dict(kw_args)

    def __hash__(self):
        return hash(a) + hash(b)

    def __eq__(self, other):
        return (self.a == other.a and
                self.b == other.b and
                self.props == other.props)

    def __str__(self):
        return str(self.iid)




def read_input():
    # n = number of cities, m = number of roads
    (n, m) = (int(i) for i in raw_input().split())
    # [] of gas prices in each city
    prices = [int(i) for i in raw_input().split()]

    # TODO: Better data structure for the graph
    roads = []
    for _ in range(m):
        # di = distance of road between city ui and vi
        (ui, vi, di) = (int(i) for i in raw_input().split())
        roads.append((ui, vi, di))

    # q = number of queries to run
    q = int(raw_input())

    # TODO: Perhaps better data structure for the queries?
    queries = []
    for _ in range(q):
        # ci = fuel capacity of vehicle, si = start city, ei = end city
        (ci, si, ei) = (int(i) for i in raw_input().split())
        queries.append((ci, si, ei))

    return (n, m, prices, roads, q, queries)


def main():
    read_input()


def test_A_star():
    G = list()
    s = Node("s")
    t = Node("t")
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")

    s.add_neighbor(a)
    s.add_neighbor(d)

    a.add_neighbor(b)
    b.add_neighbor(c)
    c.add_neighbor(t)


    pass


if __name__ == '__main__':
    main()
