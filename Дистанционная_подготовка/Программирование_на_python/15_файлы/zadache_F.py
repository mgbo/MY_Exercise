
with open('file_F.txt', 'r') as f:
	s = f.readlines()
	#print (s)
	
	l = 0
	w =''
	for i in s:
		l_i = len(i)
		if l<=l_i:
			l = l_i
			w = i

print (w)