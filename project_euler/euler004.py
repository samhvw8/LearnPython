# https://www.hackerrank.com/contests/projecteuler/challenges/euler004
def check_palindrome(num):

    l_n = map(int, str(num))
    r = l_n[::-1]
    if l_n == r:
        return True
    return False


def find_max_palindrome(num):
    max_ = 0
    for a in xrange(100, 1000):
        for b in xrange(100, 1000):
            m = a * b
            if m >= num:
                continue
            if check_palindrome(m) and m > max_:
                max_ = m
    return max_


CASE = input()
for case_i in xrange(CASE):
    max_ = input()
    print find_max_palindrome(max_)
