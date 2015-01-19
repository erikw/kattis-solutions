#!/usr/bin/env python

import sys

c = [0 for i in xrange(0, 5002)]

c[0] = 1
c[1] = 1

def catalan(n):
	if c[n] != 0:
		return c[n]

	first = 1
	second = 1
	for i in xrange(2, n + 1):
		first *= i
		second *= i

	for i in xrange(n + 1, 2*n + 1):
		second *= i

	c[n] = (second / first**2) / (n + 1)
	return c[n]

n = int(raw_input())
sn = 0

print catalan(n + 1)

