#!/usr/bin/env python

import sys

def test_base7():
    assert  base7(0) == [0]
    assert  base7(1) == [1]
    assert  base7(2) == [2]
    assert  base7(3) == [3]
    assert  base7(4) == [4]
    assert  base7(5) == [5]
    assert  base7(6) == [6]
    assert  base7(7) == [1, 0]
    assert  base7(8) == [1, 1]
    assert  base7(9) == [1, 2]
    assert  base7(10) == [1, 3]
    assert  base7(14) == [2, 0]

def test_transsym():
    assert  transsym([0]) == [0]
    assert  transsym([1]) == [1]
    assert  transsym([2]) == [2]
    assert  transsym([3]) == [5]
    assert  transsym([4]) == [6]
    assert  transsym([5]) == [8]
    assert  transsym([6]) == [9]
    assert  transsym([1, 0]) == [1, 0]
    assert  transsym([1, 1]) == [1, 1]
    assert  transsym([1, 2]) == [1, 2]
    assert  transsym([1, 3]) == [1, 5]
    assert  transsym([2, 0]) == [2, 0]

def upsidedown(num):
    res = ""
    for n in reversed(num):
        if n == 6:
            res += "9"
        elif n == 9:
            res += "6"
        else:
            res += str(n)
    return res


def base7(num):
    ret = []
    while num > 0:
        rem = num % 7
        num = num // 7
        ret.append(rem)
    if ret:
        return ret[::-1]
    else:
        return [0]

syms = [0, 1, 2, 5, 6, 8, 9]
def transsym(num7l):
    ret = []
    for n in num7l:
        ret.append(syms[n])
    return ret

def main():
    for line in sys.stdin:
        ki = int(line)

        print upsidedown(transsym(base7(ki)))



if __name__ == '__main__':
    main()
    #test_base7()
    #test_transsym()

