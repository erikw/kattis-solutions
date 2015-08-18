#!/usr/bin/env python

import sys


def main():
    T = int(raw_input())
    for _ in range(0, T):
        raw_input()
        n_cs, n_e = (int(i) for i in raw_input().split())
        iq_cs = [int(i) for i in raw_input().split()]
        iq_e  = [int(i) for i in raw_input().split()]
        avg_cs = sum(iq_cs) / float(len(iq_cs))
        avg_e  = sum(iq_e) / float(len(iq_e))
        joke_cnt = 0
        for cs in iq_cs:
            if cs < avg_cs and cs > avg_e:
                joke_cnt += 1
        print joke_cnt


if __name__ == '__main__':
    sys.exit(main())
