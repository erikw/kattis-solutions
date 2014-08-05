#!/usr/bin/env python

import sys


def main():
    inp = raw_input()
    d = dict.fromkeys(inp, 0)
    for c in inp:
        d[c] += 1
    n = 0
    l = [k for k,v in d.iteritems() if v % 2 != 0]
    while d:
        if not l or len(l) == 1:
            break
        else:
            oddchar = l[-1]
            d[oddchar] -= 1
            n += 1
            if d[oddchar] == 0:
                del l[-1]
                del d[oddchar]
    print n
    return 0


if __name__ == '__main__':
	sys.exit(main())
