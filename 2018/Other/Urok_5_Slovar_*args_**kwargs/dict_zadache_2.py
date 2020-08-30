
n = [[1,3,2,4,1,5,10,1],[2,3,5],[-1,-1,-1,-5]]
d = {}
for i in n:
	for ii in i:
		#print (ii)
		if ii not in d:
			d[ii]=1
		else:
			d[ii]+=1

'''
for k,v in (d.items()):
	print (k,v)
'''

for ii in sorted(d.keys()):
	print (ii,d[ii])



