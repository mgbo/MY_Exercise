
n = input()



def summa_sifry(n):
	res = 0
	for i in n:
		res += int(i)
	return res

print("Сумма его цифр ----> {}".format(summa_sifry(n)))

