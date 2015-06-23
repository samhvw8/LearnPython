# Problem Statement

# Lets dive into decorators! You are given N mobile numbers. Sort them in ascending order after which print them in standard format.


# +91 xxxxx xxxxx


# The given mobile numbers may have +91 or 91 or 0 written before the actual 10 digit number. Alternatively, there maynot be any prefix at all. 

# Input Format

# An integer N followed by N mobile numbers.



num = input()
l = []
for i in range(0,num):
	l.append(raw_input())

s = []

for i in l:
	if i[0] != "+":
		if len(i) == 12:

			z = "+" + i[0:2] + " " + i[2:7] + " " + i[7:]
			s.append(z)
		elif len(i) == 11:
			z = "+91" + " " + i[1:6] + " " + i[6:] 
			s.append(z)	
		elif len(i) == 10:
			z = "+91" + " " + i[0:5] + " " + i[5:]
			s.append(z)	
	else:
		z = i[0:3] + " " + i[3:8] + " " + i[8:]
		s.append(z)	


s.sort()
for i in s:
	print i