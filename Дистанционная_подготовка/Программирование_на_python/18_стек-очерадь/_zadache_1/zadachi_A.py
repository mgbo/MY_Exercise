
stack = []

while True:
	# прочитали одну строку в line
	line = input()

	if line == 'exit':
		print ('bye')
		break

	l = line.split()

	if l[0] == 'push':
		stack.append(l[1])
		print ('ok')

	elif l[0] == 'pop':
		p = stack.pop()
		print (p)

	elif l[0] == 'back':
		print (stack[-1])


	elif l[0] == 'size':
		print (len(stack))

	elif l[0] == 'clear':
		stack.clear()
		print ('ok')






