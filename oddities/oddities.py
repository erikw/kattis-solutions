#!/usr/bin/env python

import sys

def main():
    tcs = sys.stdin.readline()
    for line in sys.stdin:
        i = int(line)
        if i % 2 == 0:
            print("%d is even" % i)
        else:
            print("%d is odd" % i)
    return 0

if __name__ == '__main__':
    sys.exit(main())
