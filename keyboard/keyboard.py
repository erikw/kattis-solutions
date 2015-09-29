#!/usr/bin/env python

import sys
from pprint import pprint

cache = {} # ((sx,sy), (tx,ty)) -> distance

def shortest_path(source, target, kb_graph):
    if not cache:
        for v in kb_graph:
            for u in kb_graph:
                if u == v:
                    cache[(u, v)] = 0
                else:
                    cache[(u, v)] = sys.maxint
    if cache[(source, target)] == sys.maxint:
        dijkstra(kb_graph, source, target, cache)
    return cache[(source, target)]

def keyboard_graph(string, coord_dict, kb_graph):
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
                g[pv].append((i, 1 + shortest_path((c,d), (a,b), kb_graph)))
            i += 1
        pv_coords = pv_tmp

    g[i] = []
    for (pv, c, v) in pv_coords:
        g[pv].append((i, 0))

    return g, i

def build_graph_from_map(kb_map):
    graph = {} # (x,y) -> [(a,b),...,(c,d)]
    for y in range(len(kb_map)):
        for x in range(len(kb_map[y])):
            graph[(x,y)] = []
            # LEFT
            dx = x - 1
            while dx >= 0 and kb_map[y][x] == kb_map[y][dx]:
                dx -= 1
            if dx >= 0 and dx != x:
                graph[(x,y)].append(((dx,y), 1))
            # RIGHT
            dx = x + 1
            while dx < len(kb_map[y]) and kb_map[y][x] == kb_map[y][dx]:
                dx += 1
            if dx < len(kb_map[y]) and dx != x:
                graph[(x,y)].append(((dx,y), 1))
            # UP
            dy = y - 1
            while dy >= 0 and kb_map[y][x] == kb_map[dy][x]:
                dy -= 1
            if dy >= 0 and dy != y:
                graph[(x,y)].append(((x,dy), 1))
            # DOWN
            dy = y + 1
            while dy < len(kb_map) and kb_map[y][x] == kb_map[dy][x]:
                dy += 1
            if dy < len(kb_map) and dy != y:
                graph[(x,y)].append(((x,dy), 1))
    return graph
    

def read_input():
    r, c = [int(d) for d in raw_input().split()]
    keyboard = {} # char -> [(x,y)]
    kb_map = []
    for y in range(r):
        kb_row = raw_input().strip()
        kb_map.append(kb_row)
        for x, unit in enumerate(kb_row):
            if unit not in keyboard:
                keyboard[unit] = []
            keyboard[unit].append((x,y))
    string = raw_input().strip()
    return r, c, string, keyboard, kb_map

def dijkstra(graph, src, dst, dist=None):
    if not dist:
        dist = { (src, u): sys.maxint for u in graph }
        dist[(src, src)] = 0
    Q = set(graph) # (x,y) -> [((a,b), 1),...,((c,d), 1)]

    # TODO use prioQ
    while Q:
        u = None
        mini = sys.maxint
        for q in Q:
            if dist[(src, q)] <= mini:
                u = q
                mini = dist[(src, q)]
        Q.remove(u)

        if u is dst:
            return dist[(src, dst)]

        for mate, len_ in graph[u]:
            alt = dist[(src, u)] + len_
            if alt < dist[(src, mate)]:
                dist[(src, mate)] = alt
    return dist[(src,dst)]


def main():
    r, c, string, kb, kb_map = read_input()
    kb_graph = build_graph_from_map(kb_map)
    g, i = keyboard_graph(string + '*', kb, kb_graph)
    print dijkstra(g, 0, i)

if __name__ == '__main__':
    main()
