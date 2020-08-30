
n = input()

def ExtractDigits(n):
	new = ''
	for i in n:
		if i in '1234567890':
			new+=i
	return new


ans = ExtractDigits(n)
print (ans)