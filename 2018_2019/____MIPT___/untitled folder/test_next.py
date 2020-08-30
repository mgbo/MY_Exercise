
m = map(int, input().split()) # m: 100 150 80 200
x = next(m) # m: 150 80 200 x:100

print ("Первое число", x)

x = next(m)                     # m: 80 200          x:150
print('Второе число', x)


print('Остальные числа в цикле:')
for x in m:                     # m: 80 200
	print(x)


