#!/usr/bin/env python

import sys

gunnar = raw_input().split()
emma = raw_input().split()

ga1 = int(gunnar[0])
gb1 = int(gunnar[1])
ga2 = int(gunnar[2])
gb2 = int(gunnar[3])

ea1 = int(emma[0])
eb1 = int(emma[1])
ea2 = int(emma[2])
eb2 = int(emma[3])

ge1 = sum(xrange(ga1, gb1 + 1)) / float(gb1 - ga1 + 1)
ge2 = sum(xrange(ga2, gb2 + 1)) / float(gb2 - ga2 + 1)

gres = (ge1 + ge2) / 2

ee1 = sum(xrange(ea1, eb1 + 1)) / float(eb1 - ea1 + 1)
ee2 = sum(xrange(ea2, eb2 + 1)) / float(eb2 - ea2 + 1)

eres = (ee1 + ee2) / 2


if gres > eres:
	print "Gunnar"
elif eres > gres:
	print "Emma"
else:
	print "Tie"

sys.exit(0)
