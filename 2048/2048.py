#!/usr/bin/env python

import sys


def slide_row2(row, start, end, step):
    found_zero = False
    print range(start, end, step)
    for i in range(start, end, step):
        if row[i] == 0 or not found_zero:
            found_zero = row[i] == 0
            print 'continuing'
            continue

        j = i - step
        print 'about to loop: ', i, ', ', j
        print row
        while j >= 0 and j < len(row)-1 and not row[j]:
            print 'loop\'d'
            j -= step
        print 'replacing at: ', i, ', ', j
        if not row[j]:
            row[j] = row[i]
            row[i] = 0

    return row



def slide_col(board, d, start, end, step):
   for i in range(start, end, step):
       pass



def slide(board, d):
    """TODO"""
    if d == 0 or d == 2:
        print 'sliding row wise'
        s, e, st = (0, 4, 1) if d == 0 else (3, -1, -1)
        for row in board:
            row = slide_row2(row, s, e, st)
    elif d == 1 or d == 3:
        s, e, st = (0, 4, 1) if d == 1 else (3, -1, -1)
        print 'sliding col wise'
        for i in range(4):
            col = [0 for _ in range(4)]
            for j in range(4):
                col[j] = board[j][i]
            print 'before: ' ,col
            col = slide_row2(col, s, e, st)
            print 'after: ', col
            for j in range(4):
                board[j][i] = col[j]


def merge(board, d):
    """TODO"""
    pass

def print_board(board):
    for row in board:
        print(" ".join(str(i) for i in row))

def main():
    matrix = []
    for _ in range(4):
        line = sys.stdin.readline()
        matrix.append([int(i) for i in line.split()])

    d = int(sys.stdin.readline())
    print_board(matrix)
    slide(matrix, d)
    print_board(matrix)

    return 0


if __name__ == '__main__':
    sys.exit(main())
