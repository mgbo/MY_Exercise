
a = list(map(int,input().split()))
k = int(input())

ans = [i for i in a if i>=k]
print (*ans)