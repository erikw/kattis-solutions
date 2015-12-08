#!/usr/bin/env python

import sys
from collections import namedtuple

Show = namedtuple('Show', ['start', 'stop'])
Recorder = namedtuple('Recorder', ['id', 'end'])

def entertain_new(k, shows):
    count = 0
    shows = sorted(shows, key=lambda x: x.stop)
    recorders = [ Recorder(i, 0) for i in range(k) ]

    for show in shows:
        recorder = reduce(lambda best, rec: rec if best.end > show.start and rec.end <= show.start or rec.end > best.end and rec.end <= show.start else best, recorders, recorders[0])
        if recorder.end <= show.start:
            recorders[recorder.id] = Recorder(recorder.id, show.stop)
            count += 1

    return count

def entertain(k, shows):
    count = 0
    shows = sorted(shows, key=lambda x: x.stop)
    recorders = [ 0 ] * k
    ind = 0

    t = shows[0].start

    while ind < len(shows):
        for i in range(len(recorders)):
            rec = recorders[i]
            if rec <= t:
                recorders[i] = 0

        show = shows[ind]
        if show.stop <= t:
            # show has ended already
            ind += 1
        elif show.start == t:
            ind += 1
            try:
                i = recorders.index(0)
                recorders[i] = show.stop
                count += 1
                #print 'Choosing job {j} on recorder {i}'.format(j=show, i=i)
            except:
                #print 'Discarding job {j}'.format(j=show)
                pass

        if ind < len(shows):
            t = shows[ind].start
        #print 'New time: {t}'.format(t=t)
    return count


def main():
    _, k = [int(x) for x in raw_input().split()]
    shows = []
    for line in sys.stdin:
        start, stop = [int(x) for x in line.split()]
        shows.append(Show(start,stop))

    print entertain_new(k, shows)

if __name__ == '__main__':
	sys.exit(main())
