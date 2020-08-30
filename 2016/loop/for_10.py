
n=int(raw_input())

result=0

while n>0:
	result=result*10+n%10
	#print result
	n=n/10

print result
