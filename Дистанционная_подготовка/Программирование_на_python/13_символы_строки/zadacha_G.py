
c = input()

# print (chr(ord(c)-32)

def CaseChange(c):
	if ord(c) > 91:
		print (chr(ord(c) - 32))
	else:
		print (chr(ord(c) + 32))

CaseChange(c)