# Problem Statement

# Lets use decorators for building a name directory! You are given some information about N people. Each person has a first name, last name, age and sex. You have to print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people having the same age, the printing should be done in the order of their input. For Henry Davids, the output should be

# Mr. Henry Davids
# For Mary George, the output should be

# Ms. Mary George
# Input Format

# The first lines contain integer N followed by N lines. Each line contains firstname, lastname, age and sex separated by a single space character.


num = input()
l = []
for i in range(num):
	z = raw_input().split()
	z[2] = int(2)
	l.append(z)

l = sorted(l, key=lambda z: z[2])

for i in l:
	if i[3] == "M":
		print "Mr.", i[0], i[1]
	else:
		print "Ms.", i[0], i[1]