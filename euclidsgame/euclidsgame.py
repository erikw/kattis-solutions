#!/usr/bin/env python

import sys

def euclids_game(a, b, dp):
    if b < a:
        a,b = b,a
    if (a,b) in dp:
        return dp[(a,b)]

    if a == 0:
        return False

    m = b // a
    res0 = euclids_game(a, b - m * a, dp)
    res1 = True
    if m > 1:
        res1 = euclids_game(a, b - (m - 1) * a, dp)

    dp[(a, b)] = (res0 == False or res1 == False)
    return (res0 == False or res1 == False)


def main():
    a, b = (int(i) for i in raw_input().split())
    while a != 0 and b != 0:
        dp = dict()
        if euclids_game(a, b, dp):
            print "Stan wins"
        else:
            print "Ollie wins"
        a, b = (int(i) for i in raw_input().split())
    return 0


if __name__ == '__main__':
    sys.exit(main())
