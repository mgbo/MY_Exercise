
from math import sqrt

def time2min(h,m):
	hh = h*60 + m
	return hh
	
def min2time(hh,mm,m):
	m1 = time2min(hh,mm)
	hh = ((m+m1)//60)%24
	mm = (m+m1)%60
	
	return hh,mm

hh,mm,m = map(int,input().split())




h,m = min2time(hh,mm,m)

print (h)
print (m)
#print ("%02d:%02d"%(h,m))
