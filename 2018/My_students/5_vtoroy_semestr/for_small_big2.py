
n = int(input())
l = list(map(int, input().split()))

print (l)

def zamena(l):
	for i in range(len(l)-1):
		if i%2==0:
			if l[i]>l[i+1]:
				l[i], l[i+1] = l[i+1], l[i]
	return l

print (*(zamena(l)))
