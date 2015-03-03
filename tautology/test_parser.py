#!/usr/bin/env python

#from scanner import Scanner

from  expr import *
from  scanner import Scanner
from  parser import Parser


def test_opnp():
    p = Var("p")
    e_exp = Or(p, Not(p))
    line = "ApNp"

    test_expr(line, e_exp)

def test_apnq():
    p = Var("p")
    q = Var("q")
    e_exp = Or(p, Not(q))
    line = "ApNq"

    test_expr(line, e_exp)

def test_compl():
    #(p OR q) == p OR (NOT p AND q)
    p = Var("p")
    q = Var("q")
    e_exp = Equal(Or(p, q), Or(p, And(Not(p), q)))
    line = "EApqApKNpq"

    test_expr(line, e_exp)

def test_expr(line, e_exp):
    sc = Scanner(line)
    pr = Parser(sc)
    e_act = pr.parse()

    assert e_exp == e_act


def run_tests():
    test_opnp()
    test_apnq()
    test_compl()

if __name__ == '__main__':
    run_tests()

