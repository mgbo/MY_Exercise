def time2min(h, m):
	res = h*60 + m
	return res
	
def min2time(mm):
	h = (mm // 60) % 24
	m = mm % 60
	return h, m

def sumtime(h0, m0, mm):
	mm0 = time2min(h0, m0)	# 1
	mm1 = mm0 + mm			# 2
	h1, m1 = min2time(mm1)	# 3
	return h1, m1
	
# print(time2min(2, 15)) # 135
# print(min2time(135))  	# 2 15

h0, m0 = map(int, input().split())
mm = int(input())

#print(h0, m0, mm)

h1, m1 = sumtime(h0,m0, mm)
print("%02d:%02d" % (h1, m1))
