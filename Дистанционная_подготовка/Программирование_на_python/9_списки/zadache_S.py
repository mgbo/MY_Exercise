
l = list(map(int, input().split()))

count = 0

pair = [(l[i],l[j]) for i in range(len(l)) for j in range(len(l)-i) if l[i]==l[j] ] 

print (pair)
print (len(pair))
