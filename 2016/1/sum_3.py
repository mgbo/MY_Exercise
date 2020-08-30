
k=int(raw_input())

t=8*60+(45*k+5*(k-1))

h=(t/60)%24

m=t%60

print '%d %d'% (h,m)
