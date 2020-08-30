
n = list(map(int, input().split()))
k,m = map(int,input().split())


ans = sum([x for x in n if k<=x and m>x])
print (ans)