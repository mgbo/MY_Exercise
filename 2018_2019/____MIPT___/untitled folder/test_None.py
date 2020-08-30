
# первая строка отдельно - None

a = None
m = map(int, input().split()) # m: 100 150 80 200

for x in m:
	if a is None:
		print('Первое число ', x)
		a = x
	else:
		print ("Остальные числа в цикле : ", x)
	