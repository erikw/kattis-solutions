#!/usr/bin/env python

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


if __name__ == '__main__':
    main()
