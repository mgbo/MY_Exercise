
(lenn,step)=map(int,input().split())

path=0
i=0

while lenn-path>=step:
	path=path+step
	i=i+1
	
print lenn-path
print i
