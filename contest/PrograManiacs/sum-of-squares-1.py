import math


# https://www.hackerrank.com/contests/programaniacs-june-15/challenges/sum-of-squares-1
def sum_of_square(_l):

    _sum = 0
    for i in xrange(len(_l)):
        _sum += i**2
    return _sum


def find_sum_of_square(detail):
    if datail[0] == 1:
        if isinstance(math.sqrt(detail[1]), float):
            return 0
        else:
            return 1
    list_ = [1] * detail[0]
    sum_ = detail[1]

    for index in xrange(len(list_)):

        for i in xrange(1, math.sqrt(sum_) + 1):
            if sum_of_square(list_) == sum_:
                count += 1
            list_[index] = i


CASE  = input()
for case_i in xrange(CASE):
    detail = map(int, raw_input().split())

