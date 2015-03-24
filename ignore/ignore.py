import sys


def is_valid(n):
    #while n > 0:
        #n_i = n % 10
        #if n_i == 3 or n_i == 4 or n_i == 7:
            #return False
        #n = n // 10
    #return True

    n = str(n)
    return not ('3' in n or '4' in n or '7' in n)


def test_is_valid():
    assert not is_valid(3)
    assert not is_valid(4)
    assert not is_valid(7)
    assert not is_valid(33)
    assert is_valid(11)
    assert is_valid(12)
    assert not is_valid(14)
    assert is_valid(98)

test_is_valid()


def upsidedown(num):
    num = str(num)
    res = ""
    for n in reversed(num):
        if n == "6":
            res += "9"
        elif n == "9":
            res += "6"
        else:
            res += n

    return res


cache = {1: 1}
def main():
    for line in sys.stdin:
        ki = int(line)

        ktmp = ki
        while ktmp not in cache:
            ktmp -= 1

        i = ktmp
        out = cache[i]
        while i < ki:
            out += 1
            if is_valid(out):
                i += 1
                cache[i] = out
        print upsidedown(out)



if __name__ == '__main__':
    main()
