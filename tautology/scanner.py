
import sys

class Scanner:
    def __init__(self, line):
        self.line = line
        self.idx = 0

    def __iter__(self):
        return self

    def next(self):
        if self.idx >= len(self.line) or self.line[self.idx] == '\n':
            raise StopIteration()
        self.idx += 1
        return self.line[self.idx - 1]
