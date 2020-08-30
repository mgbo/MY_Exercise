
h1,m1 = map(int,input().split(":"))
h2,m2 = map(int,input().split(":"))

def time2min(h,m):
	hh = h*60 + m
	return hh

def min2time(ttt):
	hh = ttt//60
	mm = ttt%60
	return hh,mm

def time_sub(h1, m1, h2, m2):
	mm1 = time2min(h1, m1)
	mm2 = time2min(h2, m2)
	
	if mm2 < mm1:
		mm2 += 24*60
	
	h, m = min2time(mm2 - mm1)
	return h, m

hhh,mmm = time_sub(h1,m1,h2,m2)
print ("%02d:%02d"%(hhh,mmm))


