
'''
tuples = (1,2,'hi')

print (len(tuples))
print (tuples[2])
'''


m = [(5, 1),(5,-1),(0,0),(2, 2),(-2, -2),(3,2)]

print (m)

def dis(p):
	for i in p:
		x,y = i
		print (x,y)

dis(m)
