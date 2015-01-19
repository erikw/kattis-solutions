#!/usr/bin/env python


size = 0

def f(uncon, con, node):
    if not uncon:
        return 1.0
    if node in con:
        k = (len(con) - 1.) / (size - 1.)
        ran = next(iter(uncon)
        p0 = k * f(uncon, con, ran))
        con.add(ran)
        uncon.discard(ran)
        p1 = (1 - k) * f(uncon, con, ran)
        
        # Reset set.
        con.discard(ran)
        uncon.add(ran)
        return p0 + p1

    else:

        k = len(con) / (size - 1.)
        uncon.discard(node)
        con.add(node)

        next_node = next(iter(uncon)
        p0 = k * f(uncon, con, next_node))

        p1 = (1 - k) * f(uncon, con, )
        
        # Reset set.
        con.discard(ran)
        uncon.add(ran)
        return p0 + p1

        ????
        profit!
    

def main():
    n = int(raw_input())
    size = n
    uncon = {i for i in xrange(1, n)}
    con = set([n])
    print contract(uncon, con, n, n)

    
if __name__ == '__main__':
    main()
