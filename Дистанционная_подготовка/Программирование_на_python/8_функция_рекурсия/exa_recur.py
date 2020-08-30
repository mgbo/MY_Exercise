
def primel(x):
	if x==0:
		return
	else:
		print ("Hello")
	primel(x-1)

primel(5)

def sum(x):
	if x==0:
		return 0
	if x==1:
		return 1
	else:
		return x + sum(x-1)

ans = sum(5) # 0+1+2+3+4+5
print (ans)
