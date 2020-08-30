
a = [3,6,8,2,78,1,23,45,9]

b = sorted(a)

print (a)
print (b)

c = sorted(a, reverse=True)
print (c)

a = [3,6,-8,2,-78,1,23,-45,9]

b = sorted(a,key=abs)

print (a)
print (b)	#abs

strs = ['ccc','aaaa','d','bb']
print (sorted(strs,key=len))

strs = ['aa','BB','zz','CC']
print ("sorted str :",sorted(strs))
print ("sorted str from lower :",sorted(strs,key=str.lower))





