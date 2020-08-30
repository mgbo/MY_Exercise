
f = open('input_P.txt','r')

d = {}

for w in f:
	s_w = w.split()
	#print (s_w)
	for l in s_w:
		d[l]=d.get(l,0)+1


def sort_value(d):
	return -(int(d[1])),d[0]
print ("-------")

for k,v in sorted(d.items(),key=sort_value,reverse=False):
	print (k)


f.close()

