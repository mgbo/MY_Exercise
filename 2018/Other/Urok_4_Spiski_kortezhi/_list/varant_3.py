
#variant 3

m = [[7, 19, -3, 8, 11], [0, 56]]

mina = None
for row in m:
	if mina is None:
		mina = min(row)
	else:
		mina = min(mina, min(row))
		
print(mina)
