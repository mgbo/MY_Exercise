
#n = int(input())
num = list(map(int,input().split()))

#print (num[0])
list_even = []
list_odd = []

for i in range(num[0]):
	if i%2 == 0:
		list_even.append(num[i+1])
		print (list_even)
	else:
		list_odd.append(num[i+1])
		print (list_odd)

str_1 =' '.join(str(n) for n in list_even)
print (str_1)
print (' '.join(str(n) for n in list_odd))