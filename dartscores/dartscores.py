#!/usr/bin/env python

import sys
import math


def main():

    T = int(raw_input())

    for _ in range(T):
        n = int(raw_input())
        sum_ = 0
        for _ in range(n):
            x,y = (int(t) for t in raw_input().split())
            #print x,y
            r = math.sqrt(x*x + y*y)
            if r <= 200:
                score = min(int(11 - r / 20), 10)
                #print "x: %d, y: %d, radius: %f, score: %f" % (x, y, r, score)
                sum_ += score

        print sum_

    return 0


if __name__ == "__main__":
    sys.exit(main())

