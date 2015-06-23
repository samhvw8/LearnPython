# Problem Statement
# You are given a square matrix of size NxN. 
# Calculate the absolute difference of the sums across 
# the two main diagonals.
# Input Format
# The first line contains a single integer N. The next N lines contain N integers describing the matrix.
import math
num = int(raw_input())
l = []
for i in range(num):
	z = raw_input().split()
	z = map(int,z)
	l.append(z)

d = 0
d2 = 0
for i in range(num):
	d+=l[i][i]
	d2+=l[i][num-i-1]

print "%.0f" %math.fabs(d2-d)