
'''
Наибольшее произведение двух чисел
'''

l_n = list(map(int, input().split()))

def GreatestProduct(l_n):
	max_n = 0

	for i, n in enumerate(l_n):
		for j, nn in enumerate(l_n):
			# print ("({},{}) ----> ({},{})".format(i, n, j, nn))
			if i != j:
				mul = n*nn
				# print ("ALl Product tow number: ({},{}) ---> {}".format(n,nn,n*nn))
				if max_n < mul:
					max_n = mul
					x,y = n, nn
	
	# print (x, y)
	# return max_n
	return x,y


ans_1, ans_2 = GreatestProduct(l_n)
print (ans_1, ans_2)




