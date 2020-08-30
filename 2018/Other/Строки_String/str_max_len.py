
n = input()
print (n)

n_split=n.split()
print (n_split)

mm=0
mw=''

for x in n_split:
	ss = len(x)
	if ss>mm:
		mm=ss
		mw=x
print ("%s %d"%(mw,mm))

