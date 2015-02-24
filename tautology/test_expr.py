#!/usr/bin/env python

from expr import *
from tautology  import is_tautology

def test_var():
    v0 = Var("t0", False)
    assert not v0.eval()
    assert str(v0) == "t0"
    assert repr(v0) == "t0=False"

    v1 = Var("t1", True)
    assert v1.eval()

def test_not_expr():
    v0 = Var("t0", False)
    nexpr = Not(v0)
    assert nexpr.eval()
    nn = Not(Not(v0))
    assert not nn.eval()

def test_or_expr():
    p = Var("p", False)
    q = Var("q", True)
    or0 = Or(p, p)
    or1 = Or(p, q)
    or2 = Or(q, p)
    or3 = Or(q, q)
    assert not or0.eval()
    assert or1.eval()
    assert or2.eval()
    assert or3.eval()

def test_and_expr():
    p = Var("p", False)
    q = Var("q", True)
    and0 = And(p, p)
    and1 = And(p, q)
    and2 = And(q, p)
    and3 = And(q, q)
    assert not and0.eval()
    assert not and1.eval()
    assert not and2.eval()
    assert and3.eval()

def test_equal_expr():
    p = Var("p", False)
    q = Var("q", True)
    eq0 = Equal(p, p)
    eq1 = Equal(p, q)
    eq2 = Equal(q, p)
    eq3 = Equal(q, q)
    assert eq0.eval()
    assert not eq1.eval()
    assert not eq2.eval()
    assert eq3.eval()

def test_imply_expr():
    p = Var("p", False)
    q = Var("q", True)
    imp0 = Imply(p, p)
    imp1 = Imply(p, q)
    imp2 = Imply(q, p)
    imp3 = Imply(q, q)
    assert imp0.eval()
    assert imp1.eval()
    assert not imp2.eval()
    assert imp3.eval()

def test_collect_vars():
    p = Var("p", False)
    q = Var("q", False)
    ex0 = Or(p, Not(p))
    ex1 = Or(p, Not(q))

    v0 = ex0.collect_vars()
    v1 = ex1.collect_vars()
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

    test_taut_ornot()
    test_taut_ornot2()
    test_taut_compl()

    print "All pass."




def test_taut_ornot():
    p = Var("p")
    opnp = Or(p, Not(p))
    assert is_tautology(opnp)

def test_taut_ornot2():
    p = Var("p")
    q = Var("q")
    opnq = Or(p, Not(q))
    assert not is_tautology(opnq)

def test_taut_compl():
    #(p OR q) == p OR (NOT p AND q)
    p = Var("p")
    q = Var("q")
    oeona = Equal(Or(p, q), Or(p, And(Not(p), q)))
    assert is_tautology(oeona)


def main():
    line = raw_input()
    print line

if __name__ == '__main__':
    run_tests()
