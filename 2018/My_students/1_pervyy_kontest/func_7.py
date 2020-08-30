
from math import sqrt

def time2min(h,m):
	hh = h*60 + m
	return hh
	
h, m = map(int, input().split(':'))
mm = time2min(h, m)


print (mm)
