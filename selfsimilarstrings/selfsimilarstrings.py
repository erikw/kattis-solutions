
import sys

def similarity(s, d):
    subs = dict()

    for i in range(0, len(s) - d + 1):
        sub = s[i:d+i]
        if sub in subs:
            subs[sub] = True
        else:
            subs[sub] = False

    return all(subs.itervalues())


def main():
    for line in sys.stdin:
        line = line.strip()
        for d in range(len(line) - 1, 0, -1):
            if similarity(line, d):
                print d
                break;
        else:
            print "0"


if __name__  == '__main__':
    sys.exit(main())

