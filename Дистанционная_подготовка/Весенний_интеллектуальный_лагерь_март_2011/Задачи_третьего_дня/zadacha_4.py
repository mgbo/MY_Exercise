 
n = int(input())

l = list(map(int, input().split()))


minl = l[0]
min_ind = 0
for i in range(1,len(l)):
	if minl>l[i]:
		minl = l[i]
		min_ind = i+1

print (min_ind)




