
n = [1,2,3,5,1,10,5,7,89,4]

d={}

'''
for i in n:	
	d[i] = d.get(i,0) + 1

'''

for i in n:
	if i not in d:
		d[i]=1
	else:
		d[i]=d[i]+1


for k,v in d.items():
	print (k,v)
