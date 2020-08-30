
# -*- coding:utf-8 -*-

b=[]

f=open('bet8_1.log','r')

for line in f:
	a=map(int,line.split())
	print a
	if not a:
		break
	t3=a[1]
	b.append(t3)

print b

print '--------'

b.sort();

print "sort : ",b

first=b[0]
c=[]


print "List : ", b

count=0
count_1=0
count_2=0
count_3=0
count_4=0
count_5=0
count_6=0
count_7=0
count_8=0
count_9=0
lastline=[]



for line in b[0:]:
	#print "first :",first
	print "line : ",line
	#for y in xrange(1, 11):
	if 1==line:
	 count+=1
	if 2==line:
	 count_1+=1
	if 3==line:
	 count_2+=1
	if 4==line:
	 count_3+=1
	if 4==line:
	 count_4+=1
	if 6==line:
	 count_5+=1
	if 7==line:
	 count_6+=1
	if 8==line:
	 count_7+=1
	if 9==line:
	 count_8+=1
	if 10==line:
	 count_9+=1

print count
print count_1
print count_2
print count_3
print count_4
print count_5
print count_6
print count_7
print count_8
print count_9


newl=[]

newl.append(count)
newl.append(count_1)
newl.append(count_2)
newl.append(count_3)
newl.append(count_4)
newl.append(count_5)
newl.append(count_6)
newl.append(count_7)
newl.append(count_8)
newl.append(count_9)

print newl
maxno=max(newl)
print maxno

nn=newl.index(maxno)

print nn+1

f.close()






