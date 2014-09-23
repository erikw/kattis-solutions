#!/usr/bin/env python

def main():
    d = int(raw_input())
    
    for i in xrange(0, 200000):
        for j in xrange(i, 200000):
            val = j**2 - i**2
            if val == d:
                print "%d %d" % (i, j)
                return
            elif val > d:
                break
    print "impossible"

if __name__ == '__main__':
    main()

