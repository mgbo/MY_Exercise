
#n = [[1,3,2,4,1,5,10,1],[2,3,5]]
n = [1,2,3,4,5,1,1,10,-1]
d = {}
'''
for i in n:
	for ii in i:
		#print (ii)
		if ii not in d:
			d[ii]=1
		else:
			d[ii]+=1
'''
for ii in n:
	d[ii] = d.get(ii, 0) + 1
	#if ii not in d:
	#	d[ii]=1
	#else:
	#	d[ii]+=1

for k,v in d.items():
	print (k,v)

nn = int(input())
if nn in sorted(d.keys(), reverse=True):
	print (nn,v)
