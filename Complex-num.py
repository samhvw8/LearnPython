import math
class complex:
	def __init__(self,real,img):
		self.real = real
		self.img = img
	def conjugate(self):
		return complex(self.real,-self.img)
	def __add__(self,other):
		return complex(self.real + other.real,self.img + other.img)
	def __str__(self):
		re_str = ""
		if(self.real != 0):
			re_str += "%.2f " %(self.real)
			if(self.img > 0):
				re_str += "+ "
			if(self.img < 0):
				re_str += "- "
		if(self.img > 0):
			re_str += "%.2fi" %(self.img)
		elif(self.img < 0 and self.real != 0):
			re_str += "%.2fi" %(-self.img)
		elif(self.img < 0 and self.real == 0):
			re_str += "%.2fi" %(self.img)
		if(self.real == 0 and self.img==0):
			re_str += "0.00"
		return re_str
	def __mul__(self,other):
		real = self.real * other.real - self.img * other.img
		outer = self.real * other.img + self.img * other.real
		return complex(real,outer)
	def __sub__(self,other):
		return complex(self.real - other.real,self.img - other.img)
	def __div__(self,other):
		up = self * other.conjugate()
		down = other * other.conjugate()
		return complex(up.real/down.real,up.img/down.real)
	def mod(self):
		return math.sqrt(self.real**2 + self.img**2)

a = raw_input().split()
b = raw_input().split()
a = map(float,a)
b = map(float,b)
a = complex(a[0],a[1])
b = complex(b[0],b[1])
print a + b
print a - b
print a * b
print a / b
print "%.2f" % a.mod()
print "%.2f" % b.mod()