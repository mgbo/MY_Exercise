


def Eval(n):

	new = []
	nn = ''

	for i in n:
		if i in '0123456789':
			nn += i

		elif i not in '0123456789':
			new.append(int(nn))
			nn = ''

		if i in '+-*':
			sym.append(i)


	new.append(int(nn))

	print ("All number : {}".format(new))
	print ("mathematical symbol : {} ".format(sym))

		
	return new
	
n = input()
ans = Eval(n)
print (*ans)


