'''
a = list(map(int, input().split()))

print ('len :',len(a))

# for i in range(len(a)):
# 	print (a[i])
# print ('*'*10)

ans1 = max(a)
print ('max :',ans1)


ans2 = min(a)
print ('min :',ans2)

sum_all = sum(a)
print ('sum : ', sum_all)

b = [1,2,3,4]

aa = cmp(a,b)
print (aa)
'''


l = ['python', 'java', 'c++','c']


print (l)

l.insert(1,"dephi")
print (l)
l.remove(l[2])
print(l)

n = [1,2,3,0,9,100,-19]
n.sort()
print (n)

n.reverse()
print (n)
n.clear()
print (n)






