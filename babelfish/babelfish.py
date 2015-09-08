#!/usr/bin/env python


import sys


def main():
    d = {}
    for line in sys.stdin:
        if not line.strip():
            break
        english, foreign = [l.strip() for l in line.split()]
        d[foreign] = english

    for line in sys.stdin:
        try:
            print d[line.strip()]
        except KeyError:
            print "eh"


if __name__ == '__main__':
    main()

