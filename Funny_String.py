# Sample Input

# 2
# acxz
# bcxz
# Sample Output

# Funny
# Not Funny
# Explanation

# Consider the 1st testcase acxz

# here

# |c-a| = |x-z| = 2
# |x-c| = |c-x| = 21
# |z-x| = |a-c| = 2
# Hence Funny.

# Consider the 2st testcase bcxz

# here

# |c-b| != |x-z|
# Hence Not Funny.

def check(n):
	r = n[:]
	r.reverse()
	for i in range(1,len(n)):
		if abs(ord(n[i-1])-ord(n[i])) != abs(ord(r[i-1])-ord(r[i])):
			return 0
	return 1


num = int(raw_input())

for i in range(num):
	s = list(raw_input())
	if check(s):
		print "Funny"
	else:
		print "Not Funny"