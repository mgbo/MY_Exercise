
# -*- coding: utf-8 -*-

h = int(input("часы = "))
m = int(input("минут = "))

def time2min(h,m):
	mi=h*60+m
	return mi

def min2time(m):
	mi = m/60
	mm = m%60
	return mi,mm


mi2 = time2min(h,m)



t , m = min2time(mi2)

print ("%d:%02d"% (t,m))


