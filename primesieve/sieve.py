#!/usr/bin/env python

import math

def getprimes(n):
    sieve = [False for _ in xrange(n)]
   
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            continue
        for j in xrange (i**2, n, i):
            sieve[j] = True

    sieve[0], sieve[1] = True, True
    return {i for i,k in enumerate(sieve) if not k}

n, q = raw_input().split()
n = int(n) + 1
q = int(q)

primes = getprimes(n)
print len(primes)
for _ in xrange(q):
    p = int(raw_input())
    if p in primes:
        print 1 
    else:
        print 0
