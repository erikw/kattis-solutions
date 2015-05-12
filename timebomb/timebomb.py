#!/usr/bin/env python

import sys

digits = [
"""***
* *
* *
* *
***""",

"""  *
  *
  *
  *
  *""",

"""***
  *
***
*  
***""",

"""***
  *
***
  *
***""",

"""* *
* *
***
  *
  *""",

"""***
*  
***
  *
***""",

"""***
*  
***
* *
***""",

"""***
  *
  *
  *
  *""",

"""***
* *
***
* *
***""",

"""***
* *
***
  *
***"""
]

def main():
    firstPass = True
    i = 0
    for line in sys.stdin:
        if firstPass:
            firstPass = False
            nbrs = [ set(digits) for _ in range((len(line) + 1)/4) ]
        for nbr in nbrs:
            pattern = line[:3]
            line = line[4:]
            tmp = filter(lambda x: pattern == x.splitlines()[i], nbr)
            nbr.clear()
            nbr.update(tmp)
        i += 1

    fails = [ nbr for nbr in nbrs if not len(nbr) == 1 ]
    if fails:
        print "BOOM!!"
        return

    nbr = reduce(lambda a, x: x+a*10, [ digits.index(nbr.pop()) for nbr in nbrs ], 0)
    if nbr % 6 == 0:
        print "BEER!!"
    else:
        print "BOOM!!"
    

if __name__ == '__main__':
    main()
