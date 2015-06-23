#!/usr/bin/env python

import sys
from collections import Counter


def main():

    n = int(raw_input())
    cust = [int(i) for i in raw_input().split()]

    occurances = Counter(cust)
    uniq = [t for t in occurances if occurances[t] == 1]
    if uniq:
        imax = max(uniq)
        print cust.index(imax) + 1
    else:
        print "none"

    return 0


if __name__ == "__main__":
    sys.exit(main())
