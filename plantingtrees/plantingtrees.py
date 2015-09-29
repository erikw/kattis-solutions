#!/usr/bin/env python 

def main():
    raw_input()

    seedlings = [int(n) for n in raw_input().split()]

    seedlings.sort(reverse=True)

    for i in range(len(seedlings)):
        seedlings[i] += i + 1

    print max(seedlings) + 1

if __name__ == '__main__':
    main()
