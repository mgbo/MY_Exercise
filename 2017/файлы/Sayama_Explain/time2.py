def time2min(h, m):
	res = h*60 + m
	return res
	
def min2time(mm):
	h = (mm // 60) % 24
	m = mm % 60
	return h, m

h0, m0 = map(int, input().split())
h1, m1 = map(int, input().split())

#print("%02d:%02d" % (h0, m0))
#print("%02d:%02d" % (h1, m1))

mm0 = time2min(h0, m0)	# 1
mm1 = time2min(h1, m1)	# 2
if mm1 < mm0 :			# after 0:00
	mm1 = 24*60 + mm1
mm = mm1 - mm0			# 3
#print(mm0, mm1, mm)
h, m = min2time(mm)		# 4
print("%02d:%02d" % (h, m))


