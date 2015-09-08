#!/usr/bin/env python

import pprint


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


def main():
    r, c, string, kb = read_input()
    g, i = keyboard_graph(string + '*', kb)
    pprint.pprint(g)

if __name__ == '__main__':
    main()
