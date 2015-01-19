#!/usr/bin/env pypy

import sys


class ChessBoard(object):

    def __init__(self, sx, sy, nqueens):
        self.sx = sx
        self.sy = sy
        self.nqueens = nqueens

        # Used for debugging.
        self.queens = set()

        self.rows = set()
        self.cols = set()
        self.pdiag = set()
        self.sdiag = set()

    def add_queen(self, x, y):
        self.queens.add((x, y))
        self.rows.add(y)
        self.cols.add(x)
        self.pdiag.add(x - y)
        self.sdiag.add(self.sx - 1 - x - y)

    def print_board(self):
        for y in xrange(0, self.sy):
            for x in xrange(0, self.sx):
                if (x, y) in self.queens:
                    print "Q",
                elif self.is_free_square(x, y):
                    print 0,
                else:
                    print 1,
            print ""

    def count_free_squares(self):
        cnt = 0
        for y in xrange(0, self.sy):
            for x in xrange(0, self.sx):
                if self.is_free_square(x, y):
                    cnt += 1
        return cnt

    def is_free_square(self, x, y):
        if y in self.rows:
            return False
        if x in self.cols:
            return False
        if (x - y) in self.pdiag:
            return False
        if (self.sx - 1 - x - y) in self.sdiag:
            return False
        return True

def main():
    """Save the i:th Queen."""
    while True:
        x, y, n = map(int, sys.stdin.readline().split())

        board = ChessBoard(x, y, n)

        # Test if we should exit
        if x == 0 and y == 0 and n == 0:
            return 0

        for i in xrange(0, n):
            qx, qy = map(int, sys.stdin.readline().split())
            board.add_queen(qx - 1, qy - 1)

        cnt = board.count_free_squares()
        #board.print_board()
        print cnt


if __name__ == "__main__":
    sys.exit(main())
