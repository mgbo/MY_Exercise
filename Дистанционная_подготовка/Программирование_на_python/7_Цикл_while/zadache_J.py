
summa = 0
count = 0
while True: # бесконечный цикл
	n = int(input())
	if n <= 0:
		break
	else:
		summa+=n
		count+=1

print (summa/count)