#!/usr/bin/env python

import sys
from pprint import *


def dfs(g, freq_a, freq_b):
    stack = list([0])
    freqs = 0
    while stack:
        n = stack.pop()
        freq_b[n] = freqs
        freqs += 1
        for m in g[n]:
            stack.append(m)
            freq_a[m] = freq_b[n]
    freq_a[0] = freqs
    freq_a[g[0][0]] = freqs


def main():
    n = int(raw_input())
    g = { int(i) : [] for i in range(0, n)}
    for line in sys.stdin:
        a,b = (int(i) for i in line.split())
        g[a - 1].append(b - 1)

    freq_a = [0 for i in range(n)]
    freq_b = [0 for i in range(n)]

    dfs(g, freq_a, freq_b)

    for a, b in zip(freq_a, freq_b):
        print a,b


if __name__ == '__main__':
    sys.exit(main())
