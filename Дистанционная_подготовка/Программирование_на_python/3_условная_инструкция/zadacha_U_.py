
n = int(input('Enter a number: '))

ans1 = 0
ans2 = 0
ans3 = 0
ans4 = 0
ans5 = 0



if n//60>=1:
	ans1= str(n//60)
	n = n % 60
	print ("60 :", n)

if n/20>=1:
	ans2 = str(n//20)
	n = n%20
	print ("20 :", n)

if n/10>=1:
	ans3= str(n//10)
	n = n % 10
	print ("10 :", n)

if n/5>=1:
	ans4 = str(n//5)
	n = n % 5
	print ("5 :", n)

if n/1>=1:
	ans5= str(n//1)
	print ("1 :", n)


print (ans5, ans4, ans3, ans2, ans1)