
n = int(input())

b = ''

while n > 0:
	b = str(n % 2) + b
	print ('b ---> ',b)
	n = n//2
	print (n)

print ('final ans --->', b)
