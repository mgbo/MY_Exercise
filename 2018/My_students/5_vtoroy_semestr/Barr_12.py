
n = list(map(int,input().split()))
k,m = map(int, input().split())

#pos = list(filter(lambda x: x%2==0,nn))

'''
def myf(x):
	return k<=x<m

ans = sum(filter(myf, n))
print (ans)
'''

'''
ans1 = sum(filter(lambda x: k<=x[k:m]<m, n))
print (ans1)
'''

ans2 = sum(n[k:m])
print (ans2)