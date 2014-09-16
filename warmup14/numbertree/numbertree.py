#!/usr/bin/env python

input_ = raw_input().split()
H = input_[0]
path = ""
if len(input_) > 1:
    path = input_[1]

H = int(H) + 1

def lc(i):
    return 2 * i + 1

def rc(i):
    return lc(i) + 1

i = 0
for direction in path:

    if direction == 'L':
        i = lc(i)
    else:
        i = rc(i)

print 2 ** H - i - 1
