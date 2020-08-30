
n = int(input())
nn = list(map(int,input().split()))

#print (nn)
pos = list(filter(lambda x: x%2==0,nn))
neg = list(filter(lambda x: x%2!=0,nn))

print (*pos)
print (*neg)