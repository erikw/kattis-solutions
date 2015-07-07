#!/usr/bin/env python

import sys

def main():
    s = set()
    w,p = (int(i) for i in raw_input().split())
    l = [0]
    l.extend(int(i) for i in raw_input().split())
    l.append(w)

    for p0 in l:
        for p1 in l:
            s.add(abs(p0 - p1))

    print " ".join(str(o) for o in sorted(s)[1:])


if __name__ == "__main__":
    sys.exit(main())
