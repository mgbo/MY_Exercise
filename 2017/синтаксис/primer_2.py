
# -*- coding: utf-8 -*-

sqr = [x**2 for x in range (1,10)]

print (sqr)

def f(a, b=1):
	return a + b

ans = f(5)
print (ans)


l = [x for x in range (1,100) if x % 7 ==0 or x % 3 == 0]
print l

d = {'mega' : 10,'a': 'v', 12:'str'}
print (d['a'])

p = [1,2,3,4,5]
print p
p.append(10)
print p

p.insert(0,'chit')
print p
p.remove('chit')
print p

print ("mi"*3)

square = []
for x in range(1,10):
	square.append(x**2)

print square
