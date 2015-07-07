#!/usr/bin/env python

import sys

def cokolada_split(k, s):
    if k == s or k == 0:
        return 0
    t = 0
    if k > s:
        t = s
    return cokolada_split(k - t, s >> 1) + 1


def main():
    k = int(raw_input())
    s = 1
    while s < k:
        s <<= 1
    print s, cokolada_split(k, s)


if __name__ == "__main__":
    sys.exit(main())
