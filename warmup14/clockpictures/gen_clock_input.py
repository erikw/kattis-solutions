#!/usr/bin/env python

import random

fi = "gen.in"

written = []
with open(fi, "w") as f:
    f.write("360000\n")
    l = range(0, 360000)
    random.shuffle(l)
    l = l[:360000]
    for i in range(0, 2):
        random.shuffle(l)
        for i in range(0, 360000):
            f.write(str(l[i]) + " ")
        f.write("\n")
