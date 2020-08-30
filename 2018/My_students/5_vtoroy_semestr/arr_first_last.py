

n = int(input())
l = list(map(int, input().split()))

def change_f_l(l):
	for i in range(len(l)):
		if i%2!=0:
			l.insert(i,l[-1])
			#print ("l :",l)
			l.pop()
	return l

#print (l)

ans = change_f_l(l)
print (*ans)