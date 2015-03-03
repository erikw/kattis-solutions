#!/usr/bin/env python

import sys
from  expr import *
from  scanner import Scanner
from  parser import Parser

def is_tautology(expr):
    """Test if the given expression is a Tautology.

    Iterate in binary fashion to test all possible combinations.

    """
    variables = list(expr.collect_vars())
    [var.set_value(False) for var in variables]

    for it in xrange(2**len(variables)):
        #pprint.pprint(variables)
        i = len(variables) - 1
        while i >= 0 and variables[i]:
            variables[i].set_value(False)
            i -= 1
        variables[i].set_value(True)

        if not expr.eval():
            return False

    return True

def check_taut(line):
    sc = Scanner(line)
    pr = Parser(sc)
    expr = pr.parse()
    #print expr
    if is_tautology(expr):
        print "tautology"
    else:
        print "not"

def main():
    for line in sys.stdin:
        line = line.strip()
        if line == "0":
            break
        check_taut(line)
    return 0


if __name__ == '__main__':
    sys.exit(main())
