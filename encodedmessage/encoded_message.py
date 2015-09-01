#!/usr/bin/env python

import sys
from math import *


def main():
    raw_input()
    for line in sys.stdin:
        line = line.strip()
        sq = int(sqrt(len(line)))
        for i in range(0, sq):
            for j in range(1, sq + 1):
                sys.stdout.write(line[j*sq - i - 1])
        sys.stdout.write("\n")


if __name__ == '__main__':
    sys.exit(main())
