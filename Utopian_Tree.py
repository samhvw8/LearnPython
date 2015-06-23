#The Utopian Tree goes through 2 cycles of growth every year. 
#The first growth cycle occurs during the spring, when it doubles in height. 
#The second growth cycle occurs during the summer, 
#when its height increases by 1 meter.

#Now, a new Utopian Tree sapling is planted at the onset of spring. 
#Its height is 1 meter. Can you find the height of the tree after N growth cycles?
def UtopianTree(n,h,l):
	if (n == 0): return h;
	if(l == 0):
		return UtopianTree(n-1,h*2,1)
	elif(l == 1):
		return UtopianTree(n-1,h+1,0)

n = input()
l = []
for i in range(0,n):
	l.append(input())
for i in l:
	print UtopianTree(i,1,0)