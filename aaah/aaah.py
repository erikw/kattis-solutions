#!/usr/bin/env python


def main():
    aah = raw_input()
    target_aah = raw_input()

    if len(aah) >= len(target_aah):
        print "go"
    else:
        print "no"


if __name__ == '__main__':
    main()

