
w = input().split()

def cal(w):
	new = []
	for n in w:
		#print (n)
		if n in '0123456789':
			new.append(int(n))

		elif n in "*+-":
			a = new.pop()
			#print ("a = ",a)
			b = new.pop()
			#print ("b = ",b)

			if n=="+":
				new.append(int(b+a))
				#print (new)
			elif n== "*":
				new.append(int(b*a))
				#print (new)

			elif n == "-":
				new.append(int(b-(a)))
				#print (new)

		elif n== "=":
			print (*new)

cal(w) # 1 2 + = ---> 3



