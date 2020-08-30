

s = input()
l = len(s)

print (s)
print (l)

number = []
i = 0

while i<l:
	num=''
	symbol = s[i]
	while '0'<= symbol <='9': # symbol.isdigit()
		num+=symbol
		print ('num --->',num)
		i +=1
		if i<l:
			symbol = s[i]
			print ('------------')
		else:
			print ('+++++++++++++++')
			break
	i +=1
	if num !='':
		number.append(int(num))

print(number)



