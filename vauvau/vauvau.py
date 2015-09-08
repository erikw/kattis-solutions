#!/usr/bin/env python


def main():
    a,b,c,d = [int(i) for i in raw_input().split()]
    delivery_dudes = [int(i)-1 for i in raw_input().split()]

    for dude in delivery_dudes:
        attack0 = (dude % (a+b)) - a
        attack1 = (dude % (c+d)) - c

        if attack0 < 0 and attack1 < 0:
            print "both"
        elif attack0 < 0 or attack1 < 0:
            print "one"
        else:
            print "none"



if __name__ == '__main__':
    main()

