# Sample Input

# 2
# 12
# 1012
# Sample Output

# 2
# 3
# Explanation

# 2 digits in the number 12 divide it exactly. The first digit, 1, divides it exactly in twelve parts, and the second digit, 2 divides 12 equally in six parts.

# 1 divides 1012 exactly (and it occurs twice), and 2 also divides it exactly. Division by 0 is undefined, therefore it will not be counted.

def check(x):
	 s = str(x)
	 c = 0
	 for i in s:
	 	try:
	 		if x%int(i) == 0:
	 			c+=1
	 	except ZeroDivisionError:
	 		pass
	 return c

num = input()
for i in range(num):
	z = input()
	print check(z)
