#!/usr/bin/env python

from exceptions import *

import pprint

class Expr(object):
    def collect_vars(self):
        raise NotImplementedError

    def eval(self):
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError

class Var(Expr):
    def __init__(self, var_str, value=False):
        Expr.__init__(self)
        self.var_str = var_str
        self.value = value

    def collect_vars(self):
        return { self }

    def eval(self):
        return bool(self.value)

    def set_value(self, new_val):
        self.value = new_val

    def __str__(self):
        return self.var_str

    def __repr__(self):
        return self.var_str + "=" + str(self.value)

    def __nonzero__(self):
        return self.value

    __bool__ = __nonzero__

    def __eq__(self, other):
        return self.var_str == other.var_str and self.value == other.value

    def __hash__(self):
        return hash(self.var_str)


class Not(Expr):
    def __init__(self, ex):
        self.ex = ex

    def collect_vars(self):
        return self.ex.collect_vars()

    def eval(self):
        return not self.ex.eval()

    def __str__(self):
        return "N" + str(self.ex)

    def __eq__(self, other):
        return  self.ex == other.ex

class Or(Expr):
    def __init__(self, ex0, ex1):
        self.ex0 = ex0
        self.ex1 = ex1

    def collect_vars(self):
        return self.ex0.collect_vars() | self.ex1.collect_vars()

    def eval(self):
        return self.ex0.eval() or self.ex1.eval()

    def __str__(self):
        return "A" + str(self.ex0) + str(self.ex1)

    def __eq__(self, other):
        return  self.ex0 == other.ex0 and self.ex1 == other.ex1


class And(Expr):
    def __init__(self, ex0, ex1):
        self.ex0 = ex0
        self.ex1 = ex1

    def collect_vars(self):
        return self.ex0.collect_vars() | self.ex1.collect_vars()

    def eval(self):
        return self.ex0.eval() and self.ex1.eval()

    def __str__(self):
        return "K" + str(self.ex0) + str(self.ex1)

    def __eq__(self, other):
        return  self.ex0 == other.ex0 and self.ex1 == other.ex1


class Equal(Expr):
    def __init__(self, ex0, ex1):
        self.ex0 = ex0
        self.ex1 = ex1

    def collect_vars(self):
        return self.ex0.collect_vars() | self.ex1.collect_vars()

    def eval(self):
        return self.ex0.eval() == self.ex1.eval()

    def __str__(self):
        return "E" + str(self.ex0) + str(self.ex1)

    def __eq__(self, other):
        return  self.ex0 == other.ex0 and self.ex1 == other.ex1


class Imply(Expr):
    def __init__(self, ex0, ex1):
        self.ex0 = ex0
        self.ex1 = ex1

    def collect_vars(self):
        return self.ex0.collect_vars() | self.ex1.collect_vars()

    def eval(self):
        return not self.ex0.eval() or self.ex1.eval()

    def __str__(self):
        return "C" + str(self.ex0) + str(self.ex1)

    def __eq__(self, other):
        return  self.ex0 == other.ex0 and self.ex1 == other.ex1
