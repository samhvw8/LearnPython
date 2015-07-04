# https://www.hackerrank.com/challenges/icecream-parlor
def icecream_parlor(_m, _list):

    for num_i in xrange(len(_list)):
        num = _list[num_i]
        if num >= _m:
            continue
        find = _m - num
        if find != num:
            if find in _list[num_i + 1:]:
                print num_i + 1, _list[num_i:].index(find) + 1 + num_i
                break
        else:
            if find in _list[num_i + 1:]:
                print num_i + 1, _list[num_i + 1:].index(find) + 2 + num_i
                break
    pass


CASE = input()
for test_i in xrange(CASE):
    _m = input()
    num = input()
    num_list = map(int, raw_input().split())
    icecream_parlor(_m, num_list)

