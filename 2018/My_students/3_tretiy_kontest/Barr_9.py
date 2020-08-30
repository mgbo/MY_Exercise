
a = list(map(int,input().split()))
k,n = map(int,input().split())

ans = [a[i] for i in range(len(a)) if a[i]<k or a[i]>n]
print (*ans)