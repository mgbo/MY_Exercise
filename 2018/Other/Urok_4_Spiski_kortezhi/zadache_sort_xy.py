

m = [(5, 1),(5,-1),(0,0),(2, 2),(-2, -2),(3,2)]

print (m,'\n')

def cmpdist(p):
	x,y = p
	#dist2 = p[0]**2 + p[1]**2
	#return dist2,p[0],p[1]
	
	dist = x**2 + y**2
	print ("distance : %d ,( %d,%d)"%(dist,x,y)) 
	return dist,x,y

b = sorted(m,key=cmpdist)

print (b)
