#https://www.hackerrank.com/challenges/alternating-characters

def z(n):
	ret = 0
	for i in range(1,len(n)):
		if n[i] == n[i-1]:
			ret += 1
	return ret


num = input()
for i in range(num):
	print z(raw_input())