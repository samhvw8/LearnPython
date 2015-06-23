# Problem Statement
# You're given an array containing integer values. You need to print the fraction of count of positive numbers, negative numbers and zeroes to the total numbers. Print the value of the fractions correct to 3 decimal places.
# Input Format
# First line contains N, which is the size of the array. 
# Next line contains N integers A1,A2,A3,..,An, separated by space.
num = int(raw_input())
l = raw_input().split()
l = map(int,l)
cp = 0
cn = 0
for i in l:
	if i < 0:
		cn += 1
	elif i > 0:
		cp += 1
print "%.3f\n%.3f\n%.3f\n" %(float(cp)/num,float(cn)/num,float((num-cp-cn))/num)