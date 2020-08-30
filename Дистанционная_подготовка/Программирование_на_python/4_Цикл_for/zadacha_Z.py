
n = int(input())

l = list(int(input()) for _ in range(n-1))

for i in range(1,n+1):
	if i not in l:
		# print ("Потеряенная карточка -> {}".format(i))
		print (i)
		break

