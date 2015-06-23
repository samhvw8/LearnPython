# Sample Input

# 4  #number of test case
# abc
# abcba
# abcd
# cba

# Sample Output

# 2
# 0
# 4
# 2
# Explanation

# For the first test case, abc -> abb -> aba.
# For the second test case, abcba is already a palindromic string.
# For the third test case, abcd -> abcc -> abcb -> abca = abca -> abba.
# For the fourth test case, cba -> bba -> aba.
import math

def getreverse(string):
	s = string[:]
	l = len(s)
	for i in range(l/2):
		temp = s[i]
		s[i] = s[l-i-1]
		s[l-i-1] = temp
	return s



num = int(raw_input())

l = []
for i in range(num):
	x = list(raw_input())
	l.append(x)

for i in range(num):
	m = 0.0
	reverse = getreverse(l[i])
	for j in range(len(l[i])):
		m += math.fabs(ord(l[i][j]) - ord(reverse[j]))
	print "%.0f" %(m/2)
