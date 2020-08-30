
n = int(input())

main_d = {}

for i in range(n):
	infor = input().split(';')
	inst = infor[0]
	ostaniye = infor[1:]

	fakultet = ostaniye[0]
	ostaniye_data = ostaniye[1:]

	if inst not in main_d:
		main_d[inst] = {} # создать пустую словарь в словаре
		
		if fakultet not in main_d[inst]:
			main_d[inst][fakultet] = 1
		else:
			main_d[inst][fakultet] +=1
	else:
		if fakultet not in main_d[inst]:
			main_d[inst][fakultet] = 1
		else:
			main_d[inst][fakultet] +=1

print (main_d)

print ('-'*30)

print(main_d['MIPT']['DRAP'])
print (main_d['MIPT'])

# for k,v in main_d.items():
# 	print (k,':',end = ' ')

# 	for kk,vv in v.items():
# 		print (kk,':',vv,end= ' ')
# 	print()








