
n = input()

def EvaluationInfix(n):

	expr = list(n)
	# print (expr)
	stack = []
	num = ''

	while len(expr) > 0:
		# print ('Len ---> {}'.format(len(expr)))
		c = expr.pop(0)

		if c in '0123456789.':
			num += c
			# print ('Numbers --> '.format(num))

		else:
			if num != '':
				stack.append(num)
				# print ("STACK ---> {}".format(stack))
				num = ''
			
			if c in "+-*/":
				stack.append(c)

	return stack

'''
			else:
				num2 = stack.pop()
				op = stack.pop()
				num1 = stack.pop()

				if op == "+":
					stack.append(str(float(num1) + float(num2)))
					print ('ADD ---> {}'.format(stack))

				elif op == "-":
					stack.append(str(float(num1) - float(num2)))
					print ('SUB ---> {}'.format(stack))

				elif op == "*":
					stack.append(str(float(num1) * float(num2)))
					print ('MULTI ---> {}'.format(stack))

				elif op == "/":
					stack.append(str(float(num1) / float(num2)))
					print ('DIV ---> {}'.format(stack))
'''

# return stack

print (EvaluationInfix(n))
print (eval(n))


