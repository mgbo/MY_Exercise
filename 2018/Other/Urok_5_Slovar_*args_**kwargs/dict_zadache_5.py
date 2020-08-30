
f = open('bet.log','r')

num_chek = []

for line in f:
	chek=line[2]
	num_chek.append(chek)

print (len(num_chek))
f.close()
