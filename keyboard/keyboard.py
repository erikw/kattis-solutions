#!/usr/bin/env python 


#import pprint

def read_input():
    r, c = [int(d) for d in raw_input().split()]
    keyboard = {} # char -> [(x,y)]
    for y in range(r):
        for x, unit in enumerate(raw_input().strip()):
            if unit not in keyboard:
                keyboard[unit] = []
            keyboard[unit].append((x,y))
    string = raw_input().split()
    return r, c, string


def main():
    r, c, string = read_input()

if __name__ == '__main__':
    main()
