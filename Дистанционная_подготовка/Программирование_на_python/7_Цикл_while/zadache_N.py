
'''
f_num = 0
sec_num = 0
n = -1

while n!=0:
	n = int(input())
	if n>f_num:
		sec_num = f_num
		f_num = n
		print ("firs num : {} , sec_num : {} ".format(f_num,sec_num))

print (sec_num)
'''

first_num = 0
second_num = 0

while True:
	n = int(input())
	if n>0:
		if n>first_num:
			second_num = first_num
			first_num = n
	else:
		break

print (second_num)




	