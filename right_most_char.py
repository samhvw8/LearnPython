# https://www.codeeval.com/open_challenges/31/
import sys


def find_right_most(string, char):
    for i in range(len(string) - 1, -1, -1):
        if string[i] == char:
            return i
    return -1


test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    if test == "\n" or test == "":
        continue
    INFO = test.split(",")
    print find_right_most(INFO[0].strip(), INFO[1].strip())

test_cases.close()
