
n = list(map(int, input().split()))
m = int(input())


ans = sum([x for x in n if x<m])
print (ans)