
f = int(input())
e = int(input())
 
if f<e:
    for n in range(f,e+1):
        print (n, end = ' ')
else:
    for n in range(f,e-1,-1):
        print (n, end= ' ')
