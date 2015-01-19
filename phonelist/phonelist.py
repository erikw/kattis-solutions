#!/usr/bin/env python

import sys


class Node(object):

    def __init__(self, dig=-1):
        self.dig = dig
        self.neighbours = {}
        self.terminator = False

    def add_number(self, number):
        if len(number) == 0:
            self.terminator = True
            return len(self.neighbours) == 0

        if number[0] not in self.neighbours:
            self.neighbours[number[0]] = Node(number[0])

        if self.terminator:
            return False
        return self.neighbours[number[0]].add_number(number[1:])


def main():
    num_cases = int(sys.stdin.readline())
    for _ in range(num_cases):
        num_numbers = int(sys.stdin.readline())
        root = Node()
        i = 0
        while i < num_numbers:
            i += 1
            number = sys.stdin.readline().strip()
            if not root.add_number(number):
                print("NO")
                break
        else:
            print("YES")
        while i < num_numbers:
            sys.stdin.readline()
            i += 1




if __name__ == '__main__':
    main()
    sys.exit(0)
