#!/usr/bin/env python

from expr import *
from tautology  import is_tautology

class TestExpr(object):
    def test_var(self):
        v0 = Var("t0", False)
        assert not v0.eval()
        assert str(v0) == "t0"
        assert repr(v0) == "t0=False"

        v1 = Var("t1", True)
        assert v1.eval()

    def test_not_expr(self):
        v0 = Var("t0", False)
        nexpr = Not(v0)
        assert nexpr.eval()
        nn = Not(Not(v0))
        assert not nn.eval()

    def test_or_expr(self):
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

    def test_and_expr(self):
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

    def test_equal_expr(self):
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

    def test_imply_expr(self):
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

    def test_collect_vars(self):
        p = Var("p", False)
        q = Var("q", False)
        ex0 = Or(p, Not(p))
        ex1 = Or(p, Not(q))

        v0 = ex0.collect_vars()
        v1 = ex1.collect_vars()
        assert v0 == { p }
        assert v1 == { p, q }


    def run_tests(self):
        test_methods = [method for method in dir(self)
                               if callable(getattr(self, method)) and 'test_' in method]
        for test_method in test_methods:
            getattr(self, test_method)()
        #test_var()
        #test_not_expr()
        #test_or_expr()
        #test_and_expr()
        #test_equal_expr()
        #test_imply_expr()

        #test_collect_vars()

        #test_taut_ornot()
        #test_taut_ornot2()
        #test_taut_compl()
        #test_taut_compl2()
        #test_taut_compl3()

        print "All pass."

    def test_taut_ornot(self):
        p = Var("p")
        opnp = Or(p, Not(p))
        assert is_tautology(opnp)

    def test_taut_ornot2(self):
        p = Var("p")
        q = Var("q")
        opnq = Or(p, Not(q))
        assert not is_tautology(opnq)

    def test_taut_compl(self):
        #(p OR q) == p OR (NOT p AND q)
        p = Var("p")
        q = Var("q")
        oeona = Equal(Or(p, q), Or(p, And(Not(p), q)))
        assert is_tautology(oeona)

    def test_taut_compl2(self):
        #(p OR !p) OR (q OR !q) OR (r OR !r) OR (s OR !s) OR (t OR !t)
        p = Var("p")
        q = Var("q")
        r = Var("r")
        s = Var("s")
        t = Var("t")
        pornp = Or(p, Not(p))
        qornq = Or(q, Not(q))
        rornr = Or(r, Not(r))
        sorns = Or(s, Not(s))
        tornt = Or(t, Not(t))

        taut = Or(Or(Or(Or(pornp, qornq), rornr), sorns), tornt)
        assert is_tautology(taut)

    def test_taut_compl3(self):
        #(p AND !p) AND (q AND !q) AND (r AND !r) AND (s AND !s) AND (t AND !t)
        p = Var("p")
        q = Var("q")
        r = Var("r")
        s = Var("s")
        t = Var("t")
        pandnp = And(p, Not(p))
        qandnq = And(q, Not(q))
        randnr = And(r, Not(r))
        sandns = And(s, Not(s))
        tandnt = And(t, Not(t))

        ntaut = And(And(And(And(pandnp, qandnq), randnr), sandns), tandnt)
        assert not is_tautology(ntaut)


if __name__ == '__main__':
    TestExpr().run_tests()
