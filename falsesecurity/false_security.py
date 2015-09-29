#!/usr/bin/env python

import sys

to_morse = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    "_" : "..--",
    "." : "---.",
    "," : ".-.-",
    "?" : "----"
}

from_morse = {
    ".-"   : "A",
    "-..." : "B",
    "-.-." : "C",
    "-.."  : "D",
    "."    : "E",
    "..-." : "F",
    "--."  : "G",
    "...." : "H",
    ".."   : "I",
    ".---" : "J",
    "-.-"  : "K",
    ".-.." : "L",
    "--"   : "M",
    "-."   : "N",
    "---"  : "O",
    ".--." : "P",
    "--.-" : "Q",
    ".-."  : "R",
    "..."  : "S",
    "-"    : "T",
    "..-"  : "U",
    "...-" : "V",
    ".--"  : "W",
    "-..-" : "X",
    "-.--" : "Y",
    "--.." : "Z",
    "..--" : "_",
    "---." : ".",
    ".-.-" : ",",
    "----" : "?",
}

def main():
    for line in sys.stdin:
        line = line.strip()
        # Convert to Morse.
        lens = list()
        in_morse = ""
        for ch in line:
            in_morse += to_morse[ch]
            lens.append(len(to_morse[ch]))

        # Convert to real text.
        conv = ""
        sum_ = 0
        for l in reversed(lens):
            sign = in_morse[sum_:sum_ + l]
            sum_ += l
            conv += from_morse[sign]
        print conv

    return 0


if __name__ == '__main__':
    sys.exit(main())
