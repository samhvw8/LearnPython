# Sample Input:1

# 1
# 1
# Sample Output:1

# 1
# Sample Input:2

# 3
# 1 1 2
# Sample Output:2

# 2
# Sample Input:3

# 5
# 0 0 1 2 1
# Sample Output:3

# 2
# Explanation

# In the first input, we see only one element (1) and that element is the answer. 
# In the second input, we see three elements; 1 occurs at two places and 2 only once. Thus, the answer is 2. 
# In the third input, we see five elements. 1 and 0 occur twice. The element that occurs only once is 2.
#

def check(n):
	s = n[:]
	s = set(s)
	for i in n:
		if n.count(i) > 1:
			s.discard(i)
	for i in s:
		print i

num = input()
l = list(raw_input().split())
l = map(int,l)

check(l)