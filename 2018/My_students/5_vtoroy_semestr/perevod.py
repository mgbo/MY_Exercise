
f = open('en-ru.txt','r')

d = dict()

for letter in f:
	#print (letter)
	l = letter.split('-')
	#print (l) # list

	k = l[0].strip()
	v = l[1].strip()

	#print (k,v)

	if k.lower() not in d:
		d[k]=v
	else:
		d[k]=v
'''
for k,v in d.items():
	print (k,v)
'''

f_1 = open('input.txt','r')

s =''

for w in f_1:
	ll = w.split()
	print (ll)

	for l in ll:
		print (l)
		if l.lower() in d.keys():
			print (d[l.lower()])


f.close()
f_1.close()


