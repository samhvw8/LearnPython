# Problem Statement

# This problem is a programming version of Problem 1 from projecteuler.net

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below N.

# Input Format 
# First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.
def sum(n):
	n3 = (n-1)/3
	n5 = (n-1)/5
	n15 = (n-1)/15
	ret = n3*3*(n3+1) + n5*5*(n5+1)  - n15*15*(n15+1) 
	return ret/2
		
num = input()
l = []
for i in range(num):
	numz = input()
	l.append(numz)
for i in l:
	print sum(i)