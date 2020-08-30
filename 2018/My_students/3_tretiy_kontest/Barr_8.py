
a = list(map(int,input().split()))
k,n = map(int,input().split())

ans = [i for i in range(len(a)) if a[i]>=k and a[i]<=n]
print (*ans)