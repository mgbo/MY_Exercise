
h1,m1 = map(int,input().split(":"))
h2,m2 = map(int,input().split(":"))

def time2min(h,m):
	hh = h*60 + m
	return hh

def min2time(h1,m1,h2,m2):
	t1 = time2min(h1,m1)
	t2 = time2min(h2,m2)
	ttt = t1+t2
	
	hh = (ttt//60)%24
	mm = ttt%60
	
	return hh,mm

hhh,mmm = min2time(h1,m1,h2,m2)
print ("%02d:%02d"%(hhh,mmm))


