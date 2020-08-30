a = list(map(int,input().split()))
k,n = map(int,input().split())

b = [a[i] for i in range(len(a)) if i>=k and i<n]
print (sum(b))