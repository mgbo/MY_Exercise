
a=int(input())
b=int(input())
c=int(input())
 
if a==b==c:
    print(3)
elif a==b or b==c or a==c:
    print(2)
else:
    print(0)
 
 
 
'''
a = int(input())
b = int(input())
c = int(input())
 
count = 0
if a==b:
    if a==c:
        count = 3
    else:
        count = 2
 
if a==c:
    if a==b:
        count = 3
    else:
        count = 2
 
 
print (count)
'''