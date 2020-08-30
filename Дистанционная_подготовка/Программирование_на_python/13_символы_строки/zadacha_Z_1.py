
n = input()

def Pre_list(n):

	new = []
	nn = ''
	sym = []

	j = 0

	for i in n:
		if i in '0123456789.':
			nn += i
			# print(nn)
		else:
			new.append(int(nn))
			nn = ''

			if i in '+-*':
				new.append(i)		
	return new
	





	print (exp)

Eval(n)












