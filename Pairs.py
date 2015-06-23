# Problem Statement

# Given N integers, count the number of pairs of integers whose difference is K.

# Input Format 
# The first line contains N and K. 
# The second line contains N numbers of the set. All the N numbers are unique.

# Output Format 
# An integer that tells the number of pairs of integers whose difference is K.

#!/usr/bin/py
# Head ends here
class nodet:
	"BST node"
	def __init__(self,data):
		self.left = None
		self.right = None
		self.data = data
		self.count = 1
	def insert(self,data):
		if data < self.data:
			if self.left is None:
				self.left = nodet(data)
			else:
				self.left.insert(data)
		elif data > self.data:
			if self.right is None:
				self.right = nodet(data)
			else:
				self.right.insert(data)
		elif data == self.data:
			self.count+=1
	def search(self,data):
		if self == None:
			print "Self is node"
			return 0
		elif self.data == data:
			return 1
		elif data >self.data:
			if self.right:
				return self.right.search(data)
			else:
				return 0
		elif data < self.data:
			if self.left:
				return self.left.search(data)
			else:
				return 0
	def inorder(self):
		if self.left:
			self.left.inorder()
		print self.data
		if self.right:
			self.right.inorder()

def pairs(a,k):
	#a contains array of numbers and k is the value of difference
	answer = 0
	root = nodet(a[0])
	for i in range(1,len(a)):
		root.insert(a[i])
		# if i+k in a:
		# 	answer+=1
	for i in a:
		if root.search(i+k):
			answer+=1
	return answer
# Tail starts here
if __name__ == '__main__':
	a = map(int, raw_input().strip().split(" "))
	_a_size=a[0]
	_k=a[1]
	b = map(int, raw_input().strip().split(" "))
	print pairs(b,_k)
