
N = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = sum(a[i]*b[i] for i in range(N))
print (ans)