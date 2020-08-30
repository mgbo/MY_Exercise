
n = input()
print (n)

n_split=n.split()
print (n_split)

nl =[]
for x in n_split:
	a = x.replace('bomb','watermelon')
	nl.append(a)

print (nl)
print (" ".join(nl))