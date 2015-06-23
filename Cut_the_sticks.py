# You are given N sticks, where the length of each stick is a positive integer. A cut operation is performed on the sticks such that all of them are reduced by the length of the smallest stick.

# Suppose we have six sticks of the following lengths:

# 5 4 4 2 2 8
# Then, in one cut operation we make a cut of length 2 from each of the six sticks. For the next cut operation four sticks are left (of non-zero length), whose lengths are the following:

# 3 2 2 6
# The above step is repeated until no sticks are left.

# Given the length of N sticks, print the number of sticks that are cut in subsequent cut operations.

# Note: For each cut operation, you have to recalcuate the length of smallest sticks (excluding zero-length sticks).

# Input Format 
# The first line contains a single integer N. 
# The next line contains N integers: a0, a1,...aN-1 separated by space, where ai represents the length of ith stick.

def check(n):
	for i in n:
		if i != 0:
			return 1
	return 0
def findm(n):
	m = max(n)
	for i in n:
		if i < m and i != 0:
			m = i
	return m
num = int(raw_input())

l = list(raw_input().split())
l = map(int,l)

while check(l) == 1:
	c = 0
	cutl = findm(l)
	for i in range(len(l)):
		if l[i] > 0:
			c+= 1
			if l[i] > 1:
				l[i]-=cutl
			else: l[i] -= 1


	print c