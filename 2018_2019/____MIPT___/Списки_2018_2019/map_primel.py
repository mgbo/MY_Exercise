
m = map(int, input().split())

print (m)

for x in m:
	print(x, end=' ')


# ничего не напечатает, 
# все числа из последовательности m уже прочитали
for x in m:
    print(x, end=' ')