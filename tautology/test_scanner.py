#!/usr/bin/env python

from scanner import Scanner

def test_simple():
    line = "abcdef"
    sc = Scanner(line)
    for (e, a) in zip(line, sc):
        assert e == a

def test_ln():
    line = "\n"
    sc = Scanner(line)
    for (e, a) in zip(line, sc):
        assert e == a

def test_nil():
    line = ""
    sc = Scanner(line)
    for (e, a) in zip(line, sc):
        assert e == a

def run_tests():
    test_simple()
    test_ln()
    test_nil()


if __name__ == '__main__':
    run_tests()
