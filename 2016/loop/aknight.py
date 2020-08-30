
#n=map(int,input().split())

num = int(input())
for i in range (num):
	n=input()
t=n[-1]
print (t)
i1=0

for line in n:
	#print ("line =%d ")% line
	if t+line !=1:
		i1=i1+1
		t=1
	else:
		t=0
		
i2=len(n)-i1

#print i2

if i1<i2:
	print (i1)
else:
	print (i2)
		


