# Sample Input

# 3 
# 2147483647 
# 1 
# 0
# Sample Output

# 2147483648 
# 4294967294 
# 4294967295
# Explanation
# Take 1 for example, as unsigned 32-bits is 00000000000000000000000000000001 and doing the flipping we get 11111111111111111111111111111110 which in turn is 4294967294.

num = input()
for i in range(num):
	z = int(raw_input())
	print ~z & 0xffffffff