import math

class Goblin:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.count = 1

    def is_close(self, x, y, r):
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2) <= r

    def __str__(self):
        return str(self.x) + ", " + str(self.y) + ": " + str(self.count)

def range_compare(g, x, minY, maxY):
    g_cmp = g.x * 10001 + g.y
    minVal = x * 10001 + minY
    maxVal = x * 10001 + maxY
    if g_cmp < minVal:
        res = -1
    elif g_cmp > maxVal:
        res = 1
    else:
        res = 0
    return res

def find_between(goblins, start, end, x, minY, maxY):
    if start == end:
        return []
    while start < end:
        mid = start + (end - start) / 2
        g = goblins[mid]
        g_cmp = g.x * 10001 + g.y
        minVal = x * 10001 + minY
        maxVal = x * 10001 + maxY
        if g_cmp < minVal:
            comp = -1
        elif g_cmp > maxVal:
            comp = 1
        else:
            comp = 0
        if comp == 0:
            res = [ mid ]
            i = mid-1
            while i >= start and goblins[i].x == x and goblins[i].y >= minY:
                res.append(i)
                i -= 1
            i = mid+1
            while i < end and goblins[i].x == x and goblins[i].y <= maxY:
                res.insert(0, i)
                i += 1
            return res
        elif comp > 0:
            end = mid
        elif comp < 0:
            start = mid + 1
        else:
            return []
    return []

def main():
    nbr_goblins = int(raw_input())

    goblin_map = {}
    for i in range(nbr_goblins):
        x,y = [ int(val) for val in raw_input().split() ]
        if not (x,y) in goblin_map:
            goblin_map[(x,y)] = Goblin(x, y)
        else:
            goblin_map[(x,y)].count += 1

    goblins = list(goblin_map.itervalues())
    goblins.sort(key=lambda g: g.x * 10001 + g.y)

    count = 0

    nbr_spinklers = int(raw_input())
    for i in range(nbr_spinklers):
        x,y,r = [ int(val) for val in raw_input().split() ]

        minX = max(x - r, 0)
        maxX = min(x + r, 10000)
        minY = max(y - r, 0)
        maxY = min(y + r, 10000)

        for x_i in range(minX, maxX + 1):
            res = find_between(goblins, 0, len(goblins), x_i, minY, maxY)
            for i in res:
                g = goblins[i]
                if g.is_close(x, y, r):
                    count += g.count
                    del goblins[i]

    print nbr_goblins - count

if __name__ == "__main__":
    main()
