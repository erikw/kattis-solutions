#!/usr/bin/env python

import sys


def army_strength():
    tc = int(sys.stdin.readline())
    sys.stdin.readline()
    for _ in xrange(0, tc):
        sys.stdin.readline()
        godzilla = map(int, sys.stdin.readline().strip().split(" "))
        mecha = map(int, sys.stdin.readline().strip().split(" "))
        g_max = max(godzilla)
        m_max = max(mecha)
        if g_max >= m_max:
            print "Godzilla"
        else:
            print "MechaGodzilla"
        sys.stdin.readline()

    return 0


if __name__ == "__main__":
    sys.exit(army_strength())
