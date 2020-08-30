
#-*- coding:utf-8 -*-
# Подсчитаем, сколько раз в строке встречается каждый символ:

def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c]+=1
	for k,v in d.items():
		print(k,v)
	return d

#his = histogram('chit chit nay kaung lar')
n = input()

print (n)
print (type(n))

n_int = (n.split())

print (n_int)
print (type(n_int))

a = [1,3,4,5,6,7,8,91,1,1,2,1]
print (type(a))

ans = histogram(a)
