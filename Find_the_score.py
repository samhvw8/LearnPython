# Problem Statement
# You are given a valid XML document and you have to print its score. The first line of input is the number of XML lines followed by the XML lines. Score is given by the sum of score of each element. For any element, score is equal to the number of attributes it has.
# Input Format
# The first line shows the number of lines in XML document followed by the XML document.

import xml.etree.cElementTree as ET

def count(x):
	s = 0
	for i in x:
		if i.attrib:
			for j in i.attrib:
				s+=1
		s += count(i)
	return s

num = input()
string = ""
for i in range(0,num):
	string+=raw_input()


root = ET.fromstring(string)

s = 0
if root.attrib:
	s += 1

s += count(root)


print s