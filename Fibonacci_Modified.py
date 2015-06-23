# https://www.hackerrank.com/challenges/fibonacci-modified

INFO =  map(int, raw_input().split())
a = INFO[0]
b = INFO[1]
c = 0
for i in range(2, INFO[2]):
    a, b = b, a + b**2
print b
