

d = {}
with open ('file_AE.txt', 'r') as f:

	for i in f:
		i_s = i.strip()

		if i_s in d:
			d[i_s]+=1
		else:
			 d[i_s] = d.get(i_s,1)

total = 0 # for total votes

for v in d.values():
	total +=v

#print (total)


#k = [name for name in d.keys()]
#print (k) # all name

dd = {} # new dit

for k,v in d.items():
	if v//total>0.5:
		print (k)
	else:
		if v/total in dd: 
			dd[v/total] = k
		else:
			dd[v/total] = k

#print (dd)

res = [dd[k] for k in sorted(dd.keys(), reverse=True)]

outfile = open('output_AE.txt', 'w')


for i in res[:2]:
	print (i)
	print (i, file=outfile)

f.close()
outfile.close()







