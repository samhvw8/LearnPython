# Problem Statement

# Roy wanted to increase his typing speed for programming contests. So, his friend advised him to type the sentence "The quick brown fox jumps over the lazy dog" repeatedly, because it is a pangram. (Pangrams are sentences constructed by using every letter of the alphabet at least once.)

# After typing the sentence several times, Roy became bored with it. So he started to look for other pangrams.

# Given a sentence s, tell Roy if it is a pangram or not.

# Input Format Input consists of a line containing s.

# Constraints 
# Length of s can be at most 103 (1<= |s| <=103) and it may contain spaces, lower case and upper case letters. Lower case and upper case instances of a letter are considered the same.

# Output Format Output a line containing pangram if s is a pangram, otherwise output not pangram.
#
#

def check(n):
	for i in range(ord('a'),ord('z')+1):
		if n[chr(i)] == 0:
			return 0
	return 1

s = raw_input()

d = dict()

for i in range(ord('a'),ord('z')+1):
	z = dict.fromkeys(chr(i), 0)
	d.update(z)


for i in s:
	if i != ' ':
		if ord(i) < ord('a'):
			d[chr(ord(i)-ord('A')+ord('a'))] = 1
		else:	
			d[chr(ord(i))] = 1

if check(d):
	print "pangram"
else:
	print "not pangram"