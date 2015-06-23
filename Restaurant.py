#https://www.hackerrank.com/challenges/restaurant
def cut(n,m,i):
	if n < i or m < i:
		return 0
	elif n%i == 0 and m%i == 0:
		return 1
	elif (n*m)%(i**2) == 0:
		return cut(n-i,m,i)*cut(n,m-i,i)
	else:
		return 0

def maxcut(n):
	l = n[0]
	b = n[1]
	if l == b: return 1
	m = min(l,b)
	maxc = 0
	for i in range(1,m+1):
		if cut(l,b,i):
			maxc = (l*b)/(i**2)
	return maxc

num = input()
for i in range(num):
	l = map(int,list(raw_input().split()))
	print maxcut(l)