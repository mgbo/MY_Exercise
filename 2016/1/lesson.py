
k=int(raw_input())

sum=8*60+ (45 * k + 5 * (k-1) )

h=(sum/60)%24

m=sum%60

#print "%02d : %02d" % (h,m)

print '%d:%d '% (h,m)
