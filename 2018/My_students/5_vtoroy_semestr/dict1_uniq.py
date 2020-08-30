
num = list(map(int,input().split()))

#print (num.count(3))

uniq = []

for n in set(num):
	if num.count(n)==1:
		uniq.append(n)

print (*(sorted(uniq)))
