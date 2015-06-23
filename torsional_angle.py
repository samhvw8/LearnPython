import math

class mpoint(object):
	"""docstring for point"""
	def __init__(self, x,y,z):
		self.x = x
		self.y = y
		self.z = z
	def __add__(self,other):
		return mpoint(self.x+other.x,self.y+other.y,self.z+other.z)
	def __sub__(self,other):
		return mpoint(self.x-other.x,self.y-other.y,self.z-other.z)
	def __str__(self):
		return "Point (%.2f,%.2f,%.2f)" %(self.x,self.y,self.z)
	def move(self,dx,dy,dz):
		self.x += dx
		self.y += dy
		self.z += dz
	def distance(self,other):
		dx = self.x - other.x
		dy = self.y - other.y
		dz = self.z - other.z
		return math.sqrt(dx**2 + dy**2 + dy**2)

class mvector(object):
	"""docstring for mvector"""
	def cvector(self,A,B):
		return mvector(B.x - A.x,B.y - A.y,B.z - A.z)
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
	def __add__(self,other):
		return point(self.x+other.x,self.y+other.y,self.z+other.z)
	def __sub__(self,other):
		return point(self.x-other.x,self.y-other.y,self.z-other.z)
	def move(self,dx,dy,dz):
		self.x += dx
		self.y += dy
		self.z += dz
	def __abs__(self):
		return math.sqrt(self.x**2 + self.y**2 + self.z**2)
	def cp(self,other):
		i = self.y*other.z - self.z*other.y
		j = self.z*other.x - self.x*other.z
		z = self.x*other.y - self.y*other.x
		return mvector(i,j,z)
	def __mul__(self,other):
		return self.x*other.x + self.y*other.y + self.z*other.z



a = raw_input().split()
b = raw_input().split()
c = raw_input().split()
d = raw_input().split()

a = map(float,a)
b = map(float,b)
c = map(float,c)
d = map(float,d)

a = mpoint(a[0],a[1],a[2])
b = mpoint(b[0],b[1],b[2])
c = mpoint(c[0],c[1],c[2])
d = mpoint(d[0],d[1],d[2])

ab = mvector(0,0,0)
bc = mvector(0,0,0)
cd = mvector(0,0,0)

ab = ab.cvector(a,b)
bc = bc.cvector(b,c)
cd = cd.cvector(c,d)


x = ab.cp(bc)
y = bc.cp(cd)

phi = (x*y)/(abs(x)*abs(y))

print "%.2f" %(math.degrees(math.acos(phi)))