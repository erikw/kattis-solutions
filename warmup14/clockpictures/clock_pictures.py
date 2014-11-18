#!/usr/bin/env python

def sublistExists(list1, list2):
    return ' '.join(map(str, list2)) in ' '.join(map(str, list1))


def naive_sublist_search(l0, l1):
    for i in range(0, len(l0) - len(l1) + 1):
        in_pattern = True
        for j in range(0, len(l1)):
            if l0[i + j - 1] != l1[j]:
                in_pattern = False
                break
        if not in_pattern:
            continue
        return True # Can return index here instead.
    return False


def hash_func(seq):
    p = 11
    power = 1
    h = 0
    for i in range(0, len(seq)):
        h += power * seq[len(seq) - i - 1]
        power *= p
    return h

def rabin_karp_sublist_search(s, pattern):
    m = len(pattern)
    n = len(s)
    hs = hash_func(s[:m])
    hp = hash_func(pattern)

    print (11**(m - 1))
    for i in range(0, n - m):
        #print hs, hp, s[i:i + m], pattern
        if hs == hp:
            if s[i:i + m] == pattern:
                return True # Can return index here instead.
        hs = 11 * (hs - s[i]* 11**(m - 1)) + s[i + m]
    return False


n = int(raw_input())
c0 = [int(i) for i in raw_input().split()]
c1 = [int(i) for i in raw_input().split()]

c0.sort()
c1.sort()

c_tmp = c0[0]
for i in range(0, len(c0) - 1):
    c0[i] = c0[i + 1] - c0[i]
c0[len(c0) - 1] = 360000 - c0[len(c0) - 1]  + c_tmp

c_tmp = c1[0]
for i in range(0, len(c1) - 1):
    c1[i] = c1[i + 1] - c1[i]
c1[len(c1) - 1] = 360000 - c1[len(c1) - 1]  + c_tmp

c0 = c0 + c0
if rabin_karp_sublist_search(c0, c1):
    print "possible"
else:
    print "impossible"
