a = list(map(int,input().split()))
n = int(input())

b = [a[i] for i in range(len(a)) if a[i]<n]
print (sum(b))