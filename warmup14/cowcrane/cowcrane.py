#!/usr/bin/env python

m, l   = [int(t) + 10**8 for t in raw_input().split()]
M, L   = [int(t) + 10**8 for t in raw_input().split()]
tm, tl = [int(t) for t in raw_input().split()]

crane = 10**8

def cowrec(pos=10**8, time=0, cl=l, cm=m):
    print pos-10**8, time, cl-10**8, cm-10**8
    if time > tm or time > tl:
        print "timeout"
        return False

    if cl == L and cm == M:
        return True

    if pos == cl or pos == cm:
        if pos == cl and pos == cm:
            print "here both"
            return (cowrec(M, time + abs(pos - M), cl, M) or 
                   cowrec(L, time + abs(pos - L), L, cm))
        elif pos == cl:
            print "here pos == cl"
            return (cowrec(cm, time + abs(cm - cl), cm, cm) or 
                   cowrec(L, time + abs(L - cl), L, cm))
        elif pos == cm:
            print "here pos == cm"
            return  (cowrec(cl, time + abs(cm - cl), cl, cl) or 
                   cowrec(M, time + abs(M - cm), cl, M))
    elif cl == L:
        print "lydia done"
        return cowrec(cm, time + abs(pos - cm), cl, cm)
    elif cm == M:
        print "monica done"
        return cowrec(cl, time + abs(pos - cl), cl, cm)
    else:
        print "here"
        return (cowrec(cm, time + abs(pos - cm), cl, cm) or
                cowrec(cl, time + abs(pos - cl), cl, cm))


res = "possible" if cowrec() else "impossible"

print res

