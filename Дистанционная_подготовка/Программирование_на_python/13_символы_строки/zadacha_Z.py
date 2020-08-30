
n = input()

def Eval(n):

	new = []
	nn = ''
	# sym = []

	for i in n:
		if i in '0123456789':
			nn += i
			# print(nn)

		elif i not in '0123456789':
			new.append(int(nn))
			nn = ''

		# if i in '+-*':
		# 	sym.append(i)


	new.append(int(nn))

	print ("All number : {}".format(new))
	# print ("mathematical symbol : {} ".format(sym))

	for i,s in enumerate(sym):
		print (i,s)

		if s == '-':
			if sym[i+1] == '*':
				two = new.pop(2)
				one = new.pop(1)
				zero = new.pop(0)
				new.insert(0,zero-(one*two))

			else:
				b = new.pop(1)
				a = new.pop(0)
				# print (a,b)
				new.insert(0,a-b)

		elif s == '+':
			if sym[i+1] == '*':
				two = new.pop(2)
				one = new.pop(1)
				zero = new.pop(0)
				new.insert(0,zero+(one*two))

			else:
				b = new.pop(1)
				a = new.pop(0)
				# print (a,b)
				new.insert(0,a+b)


	
	return new
	

ans = Eval(n)
print (*ans)


