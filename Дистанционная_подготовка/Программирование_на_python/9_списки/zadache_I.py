
n = list(map(int, input().split()))

odd_l = [i for i in n if i%2 !=0]

if len(odd_l)>0:
	print (min(odd_l))

else:
	print (0)


'''
length = len(n) - 1

min_n = 1
for i in range(length):
	if n[i]%2 != 0 :
		
		# print ('odd --> {}'.format(n[i]))
		if min_n < n[i]:
			min_n = n[i]

	else:
		min_n = 0

print (min_n)
'''


