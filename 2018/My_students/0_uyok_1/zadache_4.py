
k = int(input())


h = 8 * 60
hh = (h+55*k) - 15


h1 = hh//60
m = hh%60

print ("%02d:%02d"%(h1,m))

