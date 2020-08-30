
razmer_pokupatelya = int(input())
spisok = list(map(int, input().split()))

test = 0

spisok.sort()

for i in range(len(spisok)):

	if spisok[i] < razmer_pokupatelya:
		continue

	elif spisok[i] == razmer_pokupatelya:
		test += 1
		razmer_pokupatelya = spisok[i]
		print ("Размер ноги покупателя --> {}".format(razmer_pokupatelya))

	elif spisok[i] - razmer_pokupatelya >=3:
		print (spisok[i], razmer_pokupatelya ,spisok[i] - razmer_pokupatelya)
		test +=1
		razmer_pokupatelya = spisok[i]


print (test)

