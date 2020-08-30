
condi = True
max_num = 0
i = 0

while condi:
	n = int(input())
	# print (n)
	if max_num<n:
		max_num  = n
		ind_num = i

		i +=1

	if n == 0:
		condi = False

print (ind_num)