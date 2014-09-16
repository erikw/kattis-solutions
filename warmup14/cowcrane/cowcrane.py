#!/usr/bin/env python

m, l   = [int(t) + 10**8 for t in raw_input().split()]
M, L   = [int(t) + 10**8 for t in raw_input().split()]
tm, tl = [int(t) for t in raw_input().split()]

crane = 10**8

def lydia_first():
	ttlt = abs(crane - l) + abs(L - l)
	#print "time to lydia:", ttlt
	ttmt = ttlt + abs(L - m) + abs(M - m)
	#print "time to monica:", ttmt

	return ttlt <= tl and ttmt <= tm

def monica_first():
	ttmt = abs(crane - m) + abs(M - m)
	#print "time to monica:", ttmt
	ttlt = ttmt + abs(M - l) + abs(L - l)
	#print "time to lydia:", ttlt

	return ttmt <= tm and ttlt <= tl

def bring_lydia():
	ttl = abs(crane - l) + abs(l - m)
	ttm = ttl + abs(M - m)
	ttl += abs(M - m) + abs(m - L)

	return ttm <= tm and ttl <= tl

def bring_monica():
	ttm = abs(crane - m) + abs(m - l)
	ttl = ttm + abs(L - l)
	ttm += abs(L - l) + abs(l - M)

	return ttm <= tm and ttl <= tl

res = "possible" if lydia_first() or monica_first() or bring_lydia() or bring_monica() else "impossible"

print res
