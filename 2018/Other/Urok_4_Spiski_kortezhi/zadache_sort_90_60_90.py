
m = [(90,62,92),(90,60,88),(90,60,92),(90,58,92),(91,61,91)]
#m = [[90,62,92],[90,60,88],[90,60,92],[90,58,92],[91,61,91]]
print (type(m))

def cmpdist(p):
	x,y,z = p

	dist = (x-90)**2 + (y-60)**2 + (z-90)**2
	print (dist,">>>",x,y,z)
	xx = 90 - x
	yy = y - 60
	zz = 90 -z
	
	return dist,xx,yy,zz

a = sorted(m,key=cmpdist)
print ("a :",a)





