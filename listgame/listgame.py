#!/usr/bin/env python

from math import sqrt

num = int(raw_input())
facts = 0
for i in range(2, int(sqrt(num)) + 1):
    while num != 1 and num % i == 0:
        facts += 1
        num //= i

    if num == 1:
        break

if facts == 0 or num > 1:
    facts += 1

print facts
