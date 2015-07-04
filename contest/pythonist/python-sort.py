# https://www.hackerrank.com/contests/pythonist/challenges/python-sort-sort
# Enter your code here. Read input from STDIN. Print output to STDOUT

INFO = map(int, raw_input().split())
_list = []
for i in range(INFO[0]):
    line = map(int, raw_input().split())
    _list.append(line)
    k = input()
    _list = sorted(_list, key = lambda line: line[k])
    for element in _list:
        for num in element:
            print num,
            print
