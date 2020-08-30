n = int(input())
l = list(map(int, input().split()))

new = []
lenn = len(l)

if lenn%2==0:
	len_range = lenn/2
else:
	len_range = (lenn/2)+1

for i in range(int(len_range)):
	if len(l)>=2:
		if l[0]<l[-1]:
			new.append(l[0])
			new.append(l[-1])		
			l.pop(0)
			l.pop(-1)
			#print ("------->",l)
		else:
			new.append(l[-1])		
			new.append(l[0])
			l.pop(0)
			l.pop(-1)
			#print ("------->",l)
	else:
		new.append(l[0])

print (*new)



"""
n = int(input())
l = list(map(int, input().split()))

def swap(a):
	a[0], a[1] = a[1], a[0]

def change_f_l(l):
	for i in range(len(l)-1):
		if i%2!=0:
			l.insert(i,l[-1])
			print ("l :",l)
			l.pop()
			if l[i-1]>l[i]:
				print ('({},{})'.format(l[i-1],l[i]))
				swap(l)
				print ("ll-->",l)
	return l

ans = change_f_l(l)
print (*ans)
"""