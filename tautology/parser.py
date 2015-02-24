
from expr import *

class InvalidExpression(Exception):

    def __init__(self, tok):
        super(InvalidExpression, self).__init__(tok)

class Parser():


    TOK_AND = 'K'
    TOK_OR = 'A'
    TOK_NOT = 'N'
    TOK_IMPL = 'C'
    TOK_EQ = 'E'

    TOK_VARS = {'p', 'q', 'r', 's', 't'}

    def __init__(self, scanner):
        self.scn = scanner
        self.vars = dict()  # str -> Var()

    def parse(self):
        return self._parse_expr()

    def _parse_expr(self):
        tok = next(self.scn)
        if  tok == self.TOK_AND:
            e = self._parse_and()
        elif  tok == self.TOK_OR:
            e = self._parse_or()
        elif  tok == self.TOK_NOT:
            e = self._parse_not()
        elif  tok == self.TOK_IMPL:
            e = self._parse_impl()
        elif  tok == self.TOK_EQ:
            e = self._parse_eq()
        elif tok in self.TOK_VARS:
            e = self._parse_var(tok)
        else:
            raise InvalidExpression(tok)

        return e

    def _parse_and(self):
        e0 = self._parse_expr()
        e1 = self._parse_expr()
        return And(e0, e1)

    def _parse_or(self):
        e0 = self._parse_expr()
        e1 = self._parse_expr()
        return Or(e0, e1)

    def _parse_not(self):
        e = self._parse_expr()
        return Not(e)

    def _parse_impl(self):
        e0 = self._parse_expr()
        e1 = self._parse_expr()
        return Imply(e0, e1)

    def _parse_eq(self):
        e0 = self._parse_expr()
        e1 = self._parse_expr()
        return Equal(e0, e1)

    def _parse_var(self, name):
        if name not in self.vars:
            self.vars[name] = Var(name)
        return self.vars[name]
