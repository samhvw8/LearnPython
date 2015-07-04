#!/bin/python

# Complete the function below.
# https://www.hackerrank.com/challenges/maximizing-xor

def  maxXor( l,  r):
    max_xor = 0
    for x in xrange(l, r + 1):
        for y in xrange(l, r + 1):
           xor_cur = x ^ y
           if xor_cur > max_xor:
               max_xor = xor_cur
    return max_xor
    pass



_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)
