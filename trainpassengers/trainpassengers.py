#!/usr/bin/env python

import sys

C, n = raw_input().split()
C = int(C)
n = int(n)

intrain = 0
for inp in sys.stdin:
	inp = inp.split()
	left = int(inp[0])
	entered = int(inp[1])
	waited = int(inp[2])

	intrain = intrain - left
	if intrain < 0:
		print "impossible"
		sys.exit(0)
	
	intrain += entered
	if intrain > C or intrain < C and waited > 0:
		print "impossible"
		sys.exit(0)

if intrain != 0 or waited != 0:
	print "impossible"
	sys.exit(0)

print "possible"
sys.exit(0)

