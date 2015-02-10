#!/usr/bin/env python
import sys

def digit_sum(n):
    dsum = 0
    while (n):
        dsum += n % 10
        n //= 10
    return dsum

for line in sys.stdin:
    if int(line) == 0:
        break
    N = int(line)
    p = 11
    while digit_sum(N*p) != digit_sum(N):
        p += 1
    print p
