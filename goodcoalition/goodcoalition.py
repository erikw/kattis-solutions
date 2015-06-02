#!/usr/bin/env python

def is_valid(coa):
    return reduce(lambda y, x: x[0] + y, coa, 0) > 75

def value(coa):
    return reduce(lambda y, x: x[1] * y, coa, 1)

def solve(coallitions):
    best = 0
    cache = set()

    while coallitions:
        coa = coallitions.pop()
        for party in coa:
            copy = frozenset(c for c in coa if c != party)
            if copy not in cache and is_valid(copy):
                cache.add(copy)
                val = value(copy)
                if val > best:
                    best = val
                coallitions.append(copy)
    return best

def main():
    n_testcases = int(raw_input())
    for testcase in xrange(n_testcases):
        n = int(raw_input())
        parties = set()
        for  i in xrange(n):
            s, p = (int(x) for x in raw_input().split())
            parties.add((s, float(p)/100, i))
        print solve([frozenset(parties)])*100


if __name__ == '__main__':
    main()
