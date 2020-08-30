
# Позиция
"""
Даны числа. Напечатайте их по возрастанию четных чисел, 
нечетные остаются на своих местах

"""
'''
ans = sorted(n, key=lambda x : (x%2 == 0,x))
print (ans)
'''

n = list(map(int,input().split()))

s = sorted(set([x for x in n if x%2==0] ))
print (s)

new = []
i = 0
for x in n:
	if x%2==0:
			new.append(s[i])
			i+=1
	else:
		new.append(x)

print (new)
