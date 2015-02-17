#!/usr/bin/env python

from expr import *

def test_var():
    v0 = Var("t0", False)
    assert not v0.is_tautology()
    assert str(v0) == "t0"
    assert repr(v0) == "t0=False"

    v1 = Var("t1", True)
    assert v1.is_tautology()

def test_not_expr():
    v0 = Var("t0", False)
    nexpr = Not(v0)
    assert nexpr.is_tautology()
    nn = Not(Not(v0))
    assert not nn.is_tautology()

def test_or_expr():
    p = Var("p", False)
    q = Var("q", True)
    or0 = Or(p, p)
    or1 = Or(p, q)
    or2 = Or(q, p)
    or3 = Or(q, q)
    assert not or0.is_tautology()
    assert or1.is_tautology()
    assert or2.is_tautology()
    assert or3.is_tautology()

def test_and_expr():
    p = Var("p", False)
    q = Var("q", True)
    and0 = And(p, p)
    and1 = And(p, q)
    and2 = And(q, p)
    and3 = And(q, q)
    assert not and0.is_tautology()
    assert not and1.is_tautology()
    assert not and2.is_tautology()
    assert and3.is_tautology()

def test_equal_expr():
    p = Var("p", False)
    q = Var("q", True)
    eq0 = Equal(p, p)
    eq1 = Equal(p, q)
    eq2 = Equal(q, p)
    eq3 = Equal(q, q)
    assert eq0.is_tautology()
    assert not eq1.is_tautology()
    assert not eq2.is_tautology()
    assert eq3.is_tautology()

def test_imply_expr():
    p = Var("p", False)
    q = Var("q", True)
    imp0 = Imply(p, p)
    imp1 = Imply(p, q)
    imp2 = Imply(q, p)
    imp3 = Imply(q, q)
    assert imp0.is_tautology()
    assert imp1.is_tautology()
    assert not imp2.is_tautology()
    assert imp3.is_tautology()

def test_collect_vars():
    p = Var("p", False)
    q = Var("q", False)
    ex0 = Or(p, Not(p))
    ex1 = Or(p, Not(q))

    v0 = ex0.collect_vars()
    v1 = ex1.collect_vars()
    print v0, v1
    assert v0 == { p }
    assert v1 == { p, q }


def run_tests():
    test_var()
    test_not_expr()
    test_or_expr()
    test_and_expr()
    test_equal_expr()
    test_imply_expr()

    test_collect_vars()
    print "All pass."



def test_tautology(variables, expr):
    pass


def main():
    line = raw_input()
    print line

if __name__ == '__main__':
    run_tests()
