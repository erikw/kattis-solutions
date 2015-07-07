#!/usr/bin/env python

import sys
import re


def main():
    problem = re.compile("problem", re.I)
    for line in sys.stdin:
        if problem.search(line):
            print "yes"
        else:
            print "no"
    return 0


if __name__ == "__main__":
    sys.exit(main())
