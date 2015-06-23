# Problem Statement
# You are given a valid XML document and you have to print the maximum level of nesting in it. The first line of input is the number of XML lines followed by the XML lines. Take the depth of root as 0.
# Input Format
# The first line shows the number of lines in XML document followed by the XML document.
# 

import xml.etree.cElementTree as ET
def depth(x):
	if x == None: return 0;
	else:
		d = 0
		maxd = 0
		for i in x:
			d+= 1
			if d + depth(i) > maxd:
				maxd = d + depth(i)
			d-= 1

		return maxd

num = input()
string = ""
for i in range(0,num):
	string+=raw_input()


root = ET.fromstring(string)

print depth(root)