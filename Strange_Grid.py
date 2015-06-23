#A strange grid has been recovered from an old book. 
#It has 5 columns and infinite number of rows. 
#The bottom row is considered as the first row. First few rows of the grid are like this:
#..............
#..............
#20 22 24 26 28
#11 13 15 17 19
#10 12 14 16 18
#1  3  5  7  9
#0  2  4  6  8
#The grid grows upwards forever!
#Your task is to find the integer in cth column in rth row of the grid.


def get(x,y):
	ret = 0
	if((x-1)%2 == 0):
		ret += ((x-1)/2)*10
	else:
		ret += ((x-1)/2)*10 + 1
	ret += (y-1)*2
	return ret
s = raw_input().split()
s = map(int,s)


print get(s[0],s[1])