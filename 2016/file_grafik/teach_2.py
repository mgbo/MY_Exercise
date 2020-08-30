
sl={1,2,1,1,3,5,7,8,12,45,8}
al=[1,1,2,1,3,2,1,2]

d={}

for s in sl:
	if not s in d.keys():
	 d[s]+=1
	else:
		d[s]=1

