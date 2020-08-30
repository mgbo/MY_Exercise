
#n = int(input("Вводиться чило, не меньшее 2 : "))
n = int(input())
i = 1
while i<=n:
	i+=1
	if n%i == 0:
		print (i)
		break
