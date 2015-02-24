#!/usr/bin/env python

#from scanner import Scanner

from  expr import *
from  scanner import Scanner
from  parser import Parser


def test_opnp():
    p = Var("p")
    e_exp = Or(p, Not(p))

    line = "ApNp"
    sc = Scanner(line)
    pr = Parser(sc)
    e_act = pr.parse()

    assert e_exp == e_act

def run_tests():
    test_opnp()

if __name__ == '__main__':
    run_tests()

