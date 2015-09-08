#!/usr/bin/env python

import sys

def keyboard_graph(string, coord_dict):
    """Construct the keyboard cost graph.

    """
    i = 1
    g = dict()
    g[0] = []
    pv_coords = [ (0, 0, 0) ]
    for ch in string:
        coords = coord_dict[ch]
        pv_tmp = []
        for (a, b) in coords:
            g[i] = []
            pv_tmp.append((i, a, b))
            for (pv, c, d) in pv_coords:
                g[pv].append((i, 1 + abs(c - a) + abs(d - b)))
            i += 1
        pv_coords = pv_tmp

    g[i] = []
    for (pv, c, v) in pv_coords:
        g[pv].append((i, 0))

    return g, i

def read_input():
    r, c = [int(d) for d in raw_input().split()]
    keyboard = {} # char -> [(x,y)]
    for y in range(r):
        for x, unit in enumerate(raw_input().strip()):
            if unit not in keyboard:
                keyboard[unit] = []
            keyboard[unit].append((x,y))
    string = raw_input().strip()
    return r, c, string, keyboard

def dijkstra(graph, src, dst):
    dist = { u: sys.maxint for u in graph }
    dist[src] = 0
    Q = set(graph)

    while Q:
        u = None
        mini = sys.maxint
        for q in Q:
            if dist[q] < mini:
                u = q
                mini = dist[q]
        Q.remove(u)

        if u is dst:
            return dist[dst]

        for mate, len_ in graph[u]:
            alt = dist[u] + len_
            if alt < dist[mate]:
                dist[mate] = alt
    return dist[dst]


def main():
    r, c, string, kb = read_input()
    g, i = keyboard_graph(string + '*', kb)
    print dijkstra(g, g[0], g[i])

if __name__ == '__main__':
    main()
