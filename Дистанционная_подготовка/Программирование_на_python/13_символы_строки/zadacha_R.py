

n = input()

def Eval(n):

	new = []
	nn = ''
	for i in n:
		if i in '0123456789':
			nn += i
			# print(nn)

		elif i not in '0123456789':
			new.append(int(nn))
			nn = ''

	new.append(int(nn))

	# print ("All number : {}".format(new))

	for i in n:
		if i == '*':
			b = new.pop(1)
			a = new.pop(0)

			new.insert(0,a*b)

		elif i == '+':
			b = new.pop(1)
			a = new.pop(0)

			new.insert(0,a+b)

		elif i == '-':	
			b = new.pop(1)
			a = new.pop(0)
			# print (a,b)
			new.insert(0,a-b)

	return new
	

ans = Eval(n)
print (*ans)

