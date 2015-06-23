# https://www.hackerrank.com/challenges/xoring-ninja
# Sample Input #00

# 1
# 3
# 1 2 3
# Sample Output #00

# 12
# Explanation 
# The given case will have 7 non-empty subsets whose XOR is given below

# 1=1
# 2=2
# 3=3
# 1^2=3
# 2^3=1
# 3^1=2
# 1^2^3=0
import itertools
def findsubsets(S,m):
	l = list(itertools.combinations(S, m))
	return l
def xors(n):
	ret = 0
	if type(n) is tuple:
		ret = n[0]
		for i in range(1,len(n)):
			ret^=n[i]
	else:
		if type(n) is list:
			for i in range(len(n)):
				ret+= xors(n[i])
				pass
	return ret

def sumxors(n):
	ret = 0
	for i in n:
		ret+=i
	for i in range(2,len(n)+1):
		ret = (ret + xors(findsubsets(n,i)))%1000000007
	return ret


num = input()
for i in range(num):
	maxd = input()
	l = map(long,list(raw_input().split()))
	print sumxors(l)