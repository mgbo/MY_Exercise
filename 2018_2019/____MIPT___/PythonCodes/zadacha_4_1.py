
'''
Задача 4.1: Цифры числа
Напечатайте 4 последних цифры числа в обратном порядке.

Input			Output
1279			[9, 7, 2, 1]
9876543206		[6, 0, 2, 3]
15				[5, 1, 0, 0]
'''

input_num = input()


print (input_num)

print(input_num[::-1]) # numbers in reverse order

print (input_num[:-5:-1])


def reverse_last_digits(input_num):
	new_list = []
	for n in input_num[:-5:-1]:
		new_list.append(n)

	while len(new_list)!=4:
		new_list.append(0)
		
	return new_list

ans = reverse_last_digits(input_num)
print (ans)

'''

kyaw chit thu
kyaw chit thu
kyaw chit thu
maung chit thu
maung chit thu
chit thu
chit thu
chit thu
chit thu


'''



