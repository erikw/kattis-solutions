#!/usr/bin/env python

import sys

def main():
    N, L = [int(i) for i in raw_input().split()]
    lights = list()
    prev_dist = 0
    for line in sys.stdin:
        drg = [int(i) for i in line.split()]
        dist_tmp = drg[0] - prev_dist
        prev_dist = drg[0]
        drg[0] = dist_tmp
        lights.append(drg)

    dist = 0
    time = 0
    for d, r, g in lights:
        dist += d
        time += d
        time_mod = time % (r + g)
        if time_mod < r:
            time += r - time_mod

    if dist < L:
        time += L - dist
        dist += L - dist

    print time
    

if __name__ == '__main__':
    main()
