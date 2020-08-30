
'''
import math
n = int(input())
print (math.factorial(n))
'''

n = int(input())
s=[]
summa = []
for i in range(n-1):
	#print (i+1,'*',i+2)
	s.append(str(i+1)+'*'+str(i+2))
	summa.append((i+1)*(i+2))

ans = "+".join(s)
print (ans+"="+str(sum(summa)))