
# -*- coding:utf-8 -*-
vremya=[]
pokupatel=[]
A = {}

with open('my_test.txt','r') as f:
	for line in f:
		a = line.split()
		#print (a)
		if not a:
			break
		t0 = a[0]
		cu = a[1]
		vremya.append(t0)
		pokupatel.append(cu)
		for cuu in a[1:-1]:
			#print ("cuu : ",cuu)
			A[cuu]=t0
			print (" A : ",A)
f.close()

vremya_0 = vremya[0]

print ("\nНачальное время : ",vremya_0)
print ("\nНомер покупателя : ",set(pokupatel))

N = str(input("Writer Number of customer :"))
for k,v in A.items():
	if N in k:
		ans = int(v) - int(vremya_0)
		print (ans,"Second")











