#Let's learn some new python concepts!
#You have to generate a list of the first N fibonacci numbers, 
#0 being the first number. 
#Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.


class fib:
	def __init__(self, max):
		self.max = max
	def __iter__(self): 
		self.a = 0
		self.b = 1
		self.count = 0
		return self
	def next(self): 
		fib = self.a
		if self.count > self.max:
			raise StopIteration
		self.a, self.b = self.b, self.a + self.b
		self.count+=1
		return fib

maxn = input() - 1
l = []
for x in fib(maxn):
	l.append(x**3)
print l