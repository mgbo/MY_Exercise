
f = open("tr_test.log",'r')

d={}
name=[]
dlitelna =[]

for line in f:
	s_line = line.split()
	deystviya = s_line[2]
	# хочу узнать сколько раз покупатели купили по одному
	d[deystviya]=d.get(deystviya,0)+1

	dlitelna_1=s_line[3]
	name.append(deystviya)
	dlitelna.append(dlitelna_1)

for k,v in d.items():
	print ("Названии Действии : %s ==>>> %d"%(k,v))

D = {name: ti for ti,name in zip(name,dlitelna)}

for k,v in D.items():
	print ("%s:%s"%(k,v))

N_dlitelna = []

N = input('Write name of action :')
for k in D:
	print ("D : ",D[k]) 
	if N in D[k]: # если N в значении 
		N_dlitelna.append(k)

print ("------------")
print (N_dlitelna)

N_dlitelna = [float(i) for i in N_dlitelna]
#print (sorted(N_dlitelna))
print ("Максимальная длитеность действия X : Second",min(N_dlitelna))
f.close()
