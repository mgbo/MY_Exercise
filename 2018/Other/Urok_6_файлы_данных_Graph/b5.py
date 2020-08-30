
f = open('bet.log','r')

d={}
for line in f:
	s_line = list(map(int,line.split()))
	kliyent = s_line[1]
	d[kliyent]=d.get(kliyent,0)+1


for k,v in d.items():
	print ("номер покупателей : %d ==>>> %d раз"%(k,v))


f.close()
