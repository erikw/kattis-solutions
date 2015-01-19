#!/usr/bin/env python3

m=20000
print("{:d} {:d} {:d}".format(m, m, m**2))
for i in range(1, m+1):
	for j in range(1, m+1):
	    print("{:d} {:d}".format(i, j))
print("0 0 0")
