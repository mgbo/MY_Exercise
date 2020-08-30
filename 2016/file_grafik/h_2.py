
# -*- coding:utf-8 -*-
lis_code = []
D = {}
with open('http.log','r') as f:
	for line in f:
		s = line.split()
		ss = ' '.join(s[2:])
		#print (ss)
		lis_code.append(ss)
f.close()

for i in range(len(lis_code)):
	print (lis_code[i])

print ("length : ",len(lis_code))

for j in lis_code:
	D[j] = D.get(j,0) + 1

for k,v in D.items():
	print ('{} : {}'.format(k,v))