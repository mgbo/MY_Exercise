
a = list(map(int,input().split()))

ans = [i for i in range(len(a)) if a[i]>=0]

print (*ans)