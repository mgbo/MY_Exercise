
# ------------------------ v 1 --------------------
#print(min(int(i) for i in input().split() if int(i)>0))


n = input().split()

ans = min(int(i) for i in n if int(i)>0)

print (ans)
