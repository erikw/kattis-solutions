#!/usr/bin/env python


from  datetime import *

def main():
    delta = timedelta(minutes=45)

    H, M = [int(x) for x in raw_input().split()]
    wakeup_time = datetime.combine(datetime.today(), time(H, M, 0))

    new_wakeup_time = (wakeup_time - delta).time()
    print new_wakeup_time.hour, new_wakeup_time.minute


if __name__ == '__main__':
    main()
