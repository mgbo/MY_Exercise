
# -*- coding: utf-8 -*-


h1 = int(input("часы = "))
m1 = int(input("минут = "))

h2 = int(input("часы = "))
m2 = int(input("минут = "))

def time2min(h,m):
	mi=h*60+m
	return mi%1440

def min2time(m):
	mi = (m//60)%24
	mm = m%60
	return mi,mm

def duringtime(m1,m2):
	dism =(m2-m1)
	print (dism)
	return dism
	
mi1 = time2min(h1,m1)

mi2 = time2min(h2,m2)

mi = duringtime(mi1,mi2)

t , m = min2time(mi)

print ("%d:%02d"% (t,m))
