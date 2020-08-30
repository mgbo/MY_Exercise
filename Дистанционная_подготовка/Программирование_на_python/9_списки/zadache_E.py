
a = [int(i) for i in input().split()]
for i in range(1, len(a)):

	# print(a[i-1], a[i])
    if a[i - 1] * a[i] > 0:
        print(a[i - 1], a[i])
        break


'''
n = list(map(int, input().split()))

length = len(n)
print (length)


for i in range(len(n)):
	print ('{} = {}'.format(n[i], n[(i+1)%length]))
	# print ((length - i)%length)

'''