# Problem Statement

# At the annual meeting of Board of Directors of Acme Inc, every one starts shaking hands with everyone else in the room. Given the fact that any two persons shake hand exactly once, Can you tell the total count of handshakes?

# Input Format 
# The first line contains the number of test cases T, T lines follow. 
# Each line then contains an integer N, the total number of Board of Directors of Acme.
def binomial(n, k):
	if k == 0:
		return 1
	elif 2*k > n:
		return binomial(n,n-k)
	else:
		e = n-k+1
		for i in range(2,k+1):
			e *= (n-k+i)
			e /= i
		return e

num = int(raw_input())

l = []

for i in range(num):
	n = input()
	if n == 1 or n == 0:
		print 0
	else:
		print binomial(n, 2)