
a = list(map(int, input().split()))

a_1 = [a[i+1] for i in range(a[0])]

print (*a_1[::-1])