#!/usr/bin/env python2

import sys

def verify_erased(N, orig, erased):
    if N % 2 == 0:
        return orig == erased
    else:
        for n in range(len(orig)):
            if orig[n] == erased[n]:
                return False
        return True


def main():
    N = int(raw_input())
    orig = list(sys.stdin.readline().rstrip())
    erased = list(sys.stdin.readline().rstrip())

    if verify_erased(N, orig, erased):
        print "Deletion succeeded"
    else:
        print "Deletion failed"

    return 0


if __name__ == '__main__':
    sys.exit(main())
