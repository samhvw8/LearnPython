# Problem Statement
# Let's dive into the interesting topic of regular expressions! You are given some inputs and you are required to check whether they are valid mobile numbers.
# A valid mobile number is a ten digit number starting with 7, 8 or 9.
# Input Format
# The first line contains an integer N followed by N lines, each containing some string.

def check(x):
	if not ((x[0] == 7 )or (x[0] == 8) or (x[0] == 9)):
		return 0
	return 1

num = input()
l = []
for i in range(0,num):
	string = raw_input()
	l.append(string)
for i in l:
	if(i.isdigit() and len(i) == 11):
		if(check(map(int,i))):print "YES"
		else: print "NO"
	else:
		print "NO"