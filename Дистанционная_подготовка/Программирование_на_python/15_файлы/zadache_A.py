
f = open('file_A.txt','r')
res = 0
for n in f:
	res += int(n[0])

print(res)

f.close()