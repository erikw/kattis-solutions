#!/usr/bin/env python

import sys
import itertools
from pprint import pprint

def knapsack(c, n, items):
    best_value =  0
    best_weight = 0
    best_comb = None
    for r in range(1, n+1):
        combs =  itertools.combinations(items, r)
        for comb in combs:
            weight = sum([w for (i, _, w) in comb])
            value = sum([v for (i, v, _) in comb])
            if weight <= c and  value > best_value:
                best_value = value
                best_weight = weight
                best_comb = comb
    return best_value, best_comb




def main():
    try:
        while True:
            c, n = raw_input().split()
            c =  float(c)
            n = int(n)

            inputs = []
            for i in range(n):
                v, w = raw_input().split()
                inputs.append((i, int(v), int(w)))

            bv, bc  =  knapsack(c, n, inputs)
            print len(bc)
            index_str = ""
            for c in bc:
                index_str += str(c[0])
                index_str += " "

            print index_str

    except EOFError:
        return 0

if __name__ == '__main__':
    sys.exit(main())
