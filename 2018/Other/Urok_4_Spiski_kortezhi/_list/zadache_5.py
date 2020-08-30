
'''
a = [7, 19, -3, 8 ,-11, 0 ,56]
mina = min(a)
maxa = max(a)

print (mina,maxa)

aa = [7,19,-3,8,-11]
bb = [0,56]
m = [aa, bb]

aa.extend(bb)

print (aa)


cc = (aa)
mina = min(a)
maxa = max(a)

print (mina,maxa)
'''


m = [[7, 19, -3, 8, 11], [0, 56],[-111,900],[1000,34]]

print (m)
# varian 1
mina = []
maxa = []
for row in m:
	mina.append(min(row))
	maxa.append(max(row))

print (mina)
print (maxa)

print(min(mina), max(maxa))




