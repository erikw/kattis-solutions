#!/usr/bin/env python 

def main():
    n = int(raw_input())

    for _ in range(n):
        line = raw_input()
        total = 0
        for i in range(len(line)):
            pattern = line[0:i]
            s = pattern * 70
            if s.startswith(line):
                print i
                break
        else:
            print len(line)



if __name__ == '__main__':
    main()
