#!/usr/bin/env python

from exceptions import *

class Expr(object):
    def collect_vars(self):
        raise NotImplementedError

    def eval(self):
        raise NotImplementedError

class Var(Expr):
    def __init__(self, var_str, value):
        Expr.__init__(self)
        self.var_str = var_str
        self.value = value

    def collect_vars(self):
        return { self }

    def eval(self):
        return bool(self.value)

    def __str__(self):
        return self.var_str

    def __repr__(self):
        return self.var_str + "=" + str(self.value)


class Not(Expr):
    def __init__(self, ex):
        self.ex = ex

    def collect_vars(self):
        return self.ex.collect_vars()

    def eval(self):
        return not self.ex.eval()

    def __str__(self):
        pass

class Or(Expr):
    def __init__(self, ex0, ex1):
        self.ex0 = ex0
        self.ex1 = ex1

    def collect_vars(self):
        return self.ex0.collect_vars() | self.ex1.collect_vars()

    def eval(self):
        return self.ex0.eval() or self.ex1.eval()

    def __str__(self):
        pass

class And(Expr):
    def __init__(self, ex0, ex1):
        self.ex0 = ex0
        self.ex1 = ex1

    def collect_vars(self):
        return self.ex0.collect_vars() | self.ex1.collect_vars()

    def eval(self):
        return self.ex0.eval() and self.ex1.eval()

    def __str__(self):
        pass

class Equal(Expr):
    def __init__(self, ex0, ex1):
        self.ex0 = ex0
        self.ex1 = ex1

    def collect_vars(self):
        return self.ex0.collect_vars() | self.ex1.collect_vars()

    def eval(self):
        return self.ex0.eval() == self.ex1.eval()

    def __str__(self):
        pass

class Imply(Expr):
    def __init__(self, ex0, ex1):
        self.ex0 = ex0
        self.ex1 = ex1

    def collect_vars(self):
        return self.ex0.collect_vars() | self.ex1.collect_vars()

    def eval(self):
        return not self.ex0.eval() or self.ex1.eval()

    def __str__(self):
        pass

def is_tautology(expr):
    """Test if the given expression is a Tautology.

    Iterate in binary fashion to test all possible combinations.

    """
    variables = [expr.collect_vars()]
    for var in variables:
        print var
