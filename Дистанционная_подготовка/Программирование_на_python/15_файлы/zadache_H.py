
with open('file_H.txt', 'r') as f:
	for l in f:
		l_s = l.split()
		#print (l_s) # str

		ans = [int(n) for n in l_s]
		#print (ans) # int

		print (sum(ans))

		if not f:
			break
