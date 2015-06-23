# Sample Input

# 8 5
# 2 3 1 2 3 2 3 3
# 0 3
# 4 6
# 6 7
# 3 5
# 0 7

# Sample Output

# 1
# 2
# 3
# 2
# 1
# Explanation

# Below is the representation of the lane:

#    |HIGHWAY|Lane|    ->    Width

# 0: |       |--|            2
# 1: |       |---|           3
# 2: |       |-|             1
# 3: |       |--|            2
# 4: |       |---|           3
# 5: |       |--|            2
# 6: |       |---|           3
# 7: |       |---|           3
# (0, 3): Because width[2] = 1, only the bike can pass through it.
# (4, 6): Here the largest allowed vehicle which can pass through the 5th segment is the car and for the 4th and 6th segment it's the truck. Hence the largest vehicle allowed in these segments is a car.
# (6, 7): In this example, the vehicle enters at the 6th segment and exits at the 7th segment. Both segments allow even trucks to pass through them. Hence the answer is 3.
# (3, 5): width[3] = width[5] = 2. While the 4th segment allows the truck, the 3rd and 5th allow up to a car. So 2 will be the answer here.
# (0, 7): The bike is the only vehicle which can pass through the 2nd segment, which limits the strength of the whole lane to 1.

info = raw_input().split()
info = map(int,info)

width = raw_input().split()
width = map(int,width)

t = []
for i in range(info[1]):
	z = raw_input().split()
	z = map(int,z)
	t.append(z)

for i in t:
	m = 1000
	for j in range(i[0],i[1]+1):
		if width[j] < m:
			m = width[j]
	print m