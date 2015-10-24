#!/usr/bin/env python

from collections import namedtuple, defaultdict
from heapq import *
import sys


def print_graph(G):
    """Print the graph to standard out."""
    for v in G.keys():
        for e in G[v].keys():
            print("%4d - (%3d) -> %4d" % (v, G[v][e], e))
        if not G[v]:
            print("%4d - (X)" % v)


def shortest_path(G, prices, src, dst, cap):
    """Use Dijkstra's algorithm to compute the cheapest way to the destination.

    .. Keyword Arguments:
    :param: G: The graph to traverse.
    :param: prices: The fuelling prices at each node.
    :param: src: The source node to start from.
    :param: dst: The destination.
    :param: cap: The capacity of the traveller.

    .. Types:
    :type: G: A dictionary of integers to a dictionary of integers.
    :type: prices: A dictionary mapping of integer to integers.
    :type: src: An integer.
    :type: dst: An integer.
    :type: cap: An integer.

    .. Returns:
    :returns: A tuple with a list of costs and list of previous nodes.

    """
    Vertex  = namedtuple("Vertex", ["cost", "id", "tank"])
    visited = defaultdict(lambda: False)
    cost    = defaultdict(lambda: float("inf"))

    Q = []
    cost[src, 0] = 0

    heappush(Q, Vertex(0, src, 0,))
    while Q:

        u = heappop(Q)

        if visited[u.id, u.tank]:
            continue

        if u.id == dst:
            break

        # Check if we can move to a neighboring vertex.
        if (u.tank < cap and
            u.cost + prices[u.id] < cost[u.id, u.tank+1]):
            new_cost = u.cost + prices[u.id]
            cost[u.id, u.tank+1] = new_cost
            heappush(Q, Vertex(new_cost, u.id, u.tank+1))

        for v,d in G[u.id].items():
            if (u.tank >= d and
                cost[u.id, u.tank] < cost[v, u.tank - d]):
                cost[v, u.tank - d] = cost[u.id, u.tank]
                heappush(Q, Vertex(cost[v, u.tank - d], v, u.tank - d))

        visited[u.id,u.tank] = True
    return cost[dst, 0]


def main():
    """Create a graph over several cities and compute the optimal fuel-path.

    """
    # Read the initial graph.
    n, m = (int(i) for i in sys.stdin.readline().split())
    prices = { i : int(p) for i,p in enumerate(sys.stdin.readline().split()) }
    G = { v : dict() for v in range(0, len(prices)) }
    for _ in range(0, m):
        u, v, d = (int(i) for i in sys.stdin.readline().split())
        G[u][v] = d
        G[v][u] = d

    q = int(sys.stdin.readline())
    for _ in range(0, q):
        c, s, e = (int(i) for i in sys.stdin.readline().split())
        cost = shortest_path(G, prices, s, e, c)
        if cost < float("inf"):
            print(cost)
        else:
            print("impossible")

    return 0


if __name__ == '__main__':
    sys.exit(main())
