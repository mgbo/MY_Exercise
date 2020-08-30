
def enumerates(sequnece, start=0):
	n = start
	for elem in sequnece:
		yield n,elem
		n += 1

l = ['a','b','c','d']

for i,e in enumerates(l):
	print (i,e)