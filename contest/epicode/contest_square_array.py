def fast_mod(a, b, m = 10 ** 9 + 7):
    ret = 0
    a = a % m
    b = b % m
    while b > 0:
        if b&1 != 0:
            ret += a
            if ret >= m:
                ret -= m
        a <<= 1
        if a >= m:
            a -= m
        b >>= 1
    return ret

def queries(array, mode, x, y):
    if mode == 1:
        a = 1
        b = 2
        for index in xrange(x-1,y):
            array[index] += fast_mod(a, b)
            a, b = b, b +1
        return array
    if mode == 2:
        sumz = 0
        for index in xrange(x-1,y):
            sumz += array[index]
        return fast_mod(1, sumz)


INFO = map(int, raw_input().split())
array = [0]*INFO[0]
for case in xrange(INFO[1]):
    cased = map(int, raw_input().split())
    if cased[0] == 1:
        array = queries(array, 1, cased[1], cased[2])
    if cased[0] == 2:
        print queries(array, 2, cased[1], cased[2])

