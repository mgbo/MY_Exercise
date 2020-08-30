
from math import sqrt

def min2time(m):
	hh = m/60
	mm = m%60
	
	return hh,mm

m = int(input())

h,m = min2time(m)


print ("%02d:%02d"%(h,m))
