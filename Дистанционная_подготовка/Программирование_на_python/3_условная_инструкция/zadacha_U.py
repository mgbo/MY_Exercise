
n = int(input('Enter a number: '))

ans = [0, 0, 0, 0, 0]


if n//60>=1:
	ans[4] = str(n//60)
	n = n % 60
	print ("60 :", n)

if n/20>=1:
	ans[3] = str(n//20)
	n = n%20
	print ("20 :", n)

if n/10>=1:
	ans[2] = str(n//10)
	n = n % 10
	print ("10 :", n)

if n/5>=1:
	ans[1] = str(n//5)

	n = n % 5
	print ("5 :", n)

if n//1>=1:
	ans[0]= str(n//1)
	print ("1 :", n)


print (ans)