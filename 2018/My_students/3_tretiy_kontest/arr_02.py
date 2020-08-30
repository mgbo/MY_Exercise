

def d_index(n):
	for i in range(len(n)):
		if n[i]==d:
			return i

k = int(input())
n = list(map(int,input().split()))
d = int(input())

print (d_index(n))

