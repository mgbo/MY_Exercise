

condi = True

a = 0
c = 0
b = 0

while condi:

	c = b
	b = a
	n = int(input())
	a = n

	print (f"a = {a} b = {b} c = {c}")

	if a<b and b>c:
		print ("OK -->", b)
	else:
		print ("ans : ", 0)

	if n == 0:
		condi = False





