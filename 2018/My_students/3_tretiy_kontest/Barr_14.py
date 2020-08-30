a = list(map(int,input().split()))
k,n = map(int,input().split())

b = [a[i] for i in range(len(a)) if a[i]<n and a[i]>=k]
print (sum(b))