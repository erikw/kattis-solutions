#!/usr/bin/env python

def solve(m, p, l, e, r, s, n):
    for _ in range(n):
        l_new = m * e
        p_new = l // r
        m_new = p // s
        l, p, m = l_new, p_new, m_new
    return m


def main():
    while True:
        try:
            m, p, l, e, r, s, n = [int(x) for x in raw_input().split()]
            print solve(m, p, l, e, r, s, n)
        except EOFError:
            break



if __name__ == '__main__':
    main()
