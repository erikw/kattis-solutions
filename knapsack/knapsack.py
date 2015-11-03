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



def knapsack_dp(c, n, items):
# Input:
# Values (stored in array v)
# Weights (stored in array w)
# Number of distinct items (n)
# Knapsack capacity (W)

    W = int(c) + 1
    m = [[ 0 for _ in range(W) ] for _ in range(n + 1)]

    for i in range(1, n+1):
        _, v, w = items[i-1]
        for j in range(0, W):
            if w <= j:
                m[i][j] = max(m[i-1][j], m[i-1][j-w] + v)
            else:
                m[i][j] = m[i-1][j]

    i = n
    j = W - 1
    best_comb = []
    while i > 0 and j >= 0:
        cur_val =  m[i][j]
        if cur_val ==  m[i-1][j]:
            pass
        else:
            best_comb.append((i - 1, None, None))
            j -=  items[i - 1][2]
        i -= 1


    return m[n][W-1],  best_comb

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

            # bv, bc  =  knapsack(c, n, inputs)
            bv, bc  =  knapsack_dp(c, n, inputs)
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
