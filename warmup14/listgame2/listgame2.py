#!/usr/bin/env python2

from math import sqrt

import sys
import pprint
from collections import defaultdict


def prime_factors(num):
    pfacts = defaultdict(int)
    for i in range(2, int(sqrt(num)) + 1):
        while num != 1 and num % i == 0:
            pfacts[i] += 1
            num //= i

        if num == 1:
            break

    if num > 1:
        pfacts[num] += 1

    return pfacts

def closest_triangle_nbr(t_n):
    return int(-0.5 + sqrt(8 * t_n + 1) / 2)

def triangle_number(n):
    return n * (n + 1) // 2

def stirling2(n, k):
    if n == k == 0:
        return 1
    elif n == 0 or k == 0:
        return 0
    else:
        return k * stirling2(n - 1, k) + stirling2(n - 1, k - 1)

def bell(n):
    b = 0
    for k in range(0,n+1):
        b += stirling2(n, k)
    return b


def main():
    points = 0
    num = int(raw_input())
    pfacts = prime_factors(num)
    pprint.pprint(pfacts)
    sum_rest = 0
    sum_invalid = 0
    for p, e in pfacts.iteritems():
        nth_trigno = closest_triangle_nbr(e)
        points += nth_trigno
        rest = e - triangle_number(nth_trigno)
        sum_rest += rest
        sum_invalid += bell(rest)
    bell_sum = bell(sum_rest)
    print "bell sum = %d" % bell_sum
    print "sum_invalid =  %d" % sum_invalid
    points += bell_sum - sum_invalid
    print "points = %d" % points

    return 0

if __name__ == '__main__':
    sys.exit(main())
