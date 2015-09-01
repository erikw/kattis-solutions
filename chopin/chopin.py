#!/usr/bin/env python

import sys

notes = {
    "A"        : "UNIQUE",
    "A minor"  : "UNIQUE",
    "A major"  : "UNIQUE",

    "A#"       : "Bb",
    "A# minor" : "Bb minor",
    "A# major" : "Bb major",

    "Bb"       : "A#",
    "Bb minor" : "A# minor",
    "Bb major" : "A# major",

    "B"        : "UNIQUE",
    "B minor"  : "UNIQUE",
    "B major"  : "UNIQUE",

    "C"        : "UNIQUE",
    "C minor"  : "UNIQUE",
    "C major"  : "UNIQUE",

    "C#"       : "Db",
    "C# minor" : "Db minor",
    "C# major" : "Db major",

    "Db"       : "C#",
    "Db minor" : "C# minor",
    "Db major" : "C# major",

    "D"        : "UNIQUE",
    "D minor"  : "UNIQUE",
    "D major"  : "UNIQUE",

    "D#"       : "Eb",
    "D# minor" : "Eb minor",
    "D# major" : "Eb major",

    "Eb"       : "D#",
    "Eb minor" : "D# minor",
    "Eb major" : "D# major",

    "E"        : "UNIQUE",
    "E minor"  : "UNIQUE",
    "E major"  : "UNIQUE",

    "F"        : "UNIQUE",
    "F minor"  : "UNIQUE",
    "F major"  : "UNIQUE",

    "F#"       : "Gb",
    "F# minor" : "Gb minor",
    "F# major" : "Gb major",

    "Gb"       : "F#",
    "Gb minor" : "F# minor",
    "Gb major" : "F# major",

    "G"        : "UNIQUE",
    "G minor"  : "UNIQUE",
    "G major"  : "UNIQUE",

    "G#"       : "Ab",
    "G# minor" : "Ab minor",
    "G# major" : "Ab major",

    "Ab"       : "G#",
    "Ab minor" : "G# minor",
    "Ab major" : "G# major",
}

def main():
    for i, line in enumerate(sys.stdin, start=1):
        print("Case %d: %s" % (i, notes[line.strip()]))

if __name__ == '__main__':
    sys.exit(main())
