
f = open('bet.log','r')

novyye_zapisi = []

for line in f:
	#print ("line : ",line)
	l_s = line.split()
	#print ("l_s : ",l_s)
	nomer_zapisi = l_s[2]
	#print (nomer_zapisi)
	novyye_zapisi.append(nomer_zapisi)

print (novyye_zapisi)

f_zapisi=novyye_zapisi[0]

for s_zapisi in novyye_zapisi[1:]:
	if s_zapisi>f_zapisi:
		print ("f_zapisi : ",f_zapisi)
		f_zapisi=s_zapisi
		print ("s_zapisi : ",s_zapisi)
		print ("OK")
	else:
		print ("f_zapisi : ",f_zapisi)
		f_zapisi=s_zapisi
		print ("s_zapisi : ",s_zapisi)
		print ("Not OK")
		break
else:
	print ("OK!!!!")

f.close()
