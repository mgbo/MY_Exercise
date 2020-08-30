
'''
a,b = map(int,input().split(":"))


def time2min(a,b):
	res=a*60+b
	return res

ans = time2min(a,b)
print (ans)

'''


'''
def hm(m):
	h=m/60
	m1=m%60
	return h,m1

res1,res2 = hm(m)
res3,res4 =hm(mm)

print ("часы 1 , %02d:%02d"%(res1,res2))
print ("часы 2 , %02d:%02d"%(res3,res4))

'''


from math import sqrt

x1,y1,x2,y2 = map(int,input().split())

def len(a,b,c,d):
	res = sqrt((a-c)*(a-c) + (b-d)*(b-d))
	return res
	
ans = len(x1,y1,x2,y2)

print ("the length is %d meter"%ans)

x3,y3,x4,y4 = map(int,input().split())
ans2 = len(x3,y3,x4,y4)

print ("the length is %d meter"%ans2)

