
'''
Задача 4.2: Цифры числа в прямом порядке
Напечатайте 4 последних цифры числа в обратном порядке.

Input			Output
1279			[1, 2, 7, 9]
9876543206		[3, 2, 0, 6]
15				[0, 0, 1, 5]

'''

input_num = input()


print (input_num)

print(input_num[-4::]) # 4 last numbers


def reverse_last_digits(input_num):
	new_list = []
	for n in input_num[-5::]:
		new_list.append(n)

	while len(new_list) != 4:
		new_list.insert(0,0)

	return new_list

ans = reverse_last_digits(input_num)
print (ans)






