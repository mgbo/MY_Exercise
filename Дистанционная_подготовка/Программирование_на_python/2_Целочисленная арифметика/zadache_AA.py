
h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())
h3 = int(input())
m3 = int(input())

tm_1 = h1*60 + m1
tm_2 = h2*60 + m2
tm_3 = h3*60 + m3

if tm_3<tm_2:
	tm_3 = tm_3 + 24*60

if tm_2<tm_1:
	tm_2 = tm_2 + 24*60

if tm_3<tm_2:
	tm_3 = tm_3 + 24*60

diff_t1 = tm_2 - tm_1
print (diff_t1)

diff_t2 = tm_1 - diff_t1
print (diff_t2)

t = (tm_3 - diff_t2)*2

diff_t1 = diff_t2 + t

res_h = (diff_t1/60)
res_m = (diff_t1%60)

print ('{:d}:{:d}'.format(res_h,res_m))












