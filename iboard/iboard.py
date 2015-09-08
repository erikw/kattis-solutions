#!/usr/bin/env python

import sys


def count_bits(i, one_down, zero_down):
    for _ in range(7):
        if i & 1:
            one_down = not one_down
        else:
            zero_down = not zero_down 
        i = i >> 1

    return one_down, zero_down


def main():
    for line in sys.stdin:
        line = line.strip()

        if (len(line) * 7) % 2:
            print "trapped"
            continue

        one_down = False
        zero_down = False

        for c in line:
            one_down, zero_down = count_bits(ord(c), one_down, zero_down)

        if one_down or zero_down:
            print "trapped"
        else:
            print "free"


if __name__ == '__main__':
    main()
