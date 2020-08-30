
n = int(input())

def input_num(n):
	l = []
	for i in range(n):
		l.append(int(input()))
	return l


ans = input_num(n)
# print (ans)

min_num = ans[0]

for i in ans[1:]:
	if min_num > i:
		min_num = i

print (min_num)



