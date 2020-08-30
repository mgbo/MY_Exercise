
#~ def f(n,pric,d):
	#~ pric=pric+1
	#~ if n>pric:
	#~ n=n-pric
	#~ d=d+1
	
	#~ return n,pric,d


def obed(n, price, d):
	print ('eat day=%d price=%d n=%d' % (d, price, n))
	if price > n :
		return d-1
	# eating
	n_new = n - price;
	d_new = d + 1
	price_new = price + 1;
	d_new = obed(n_new, price_new, d+1)	
	
	return d_new
	
(n0,pric0)=map(int,input().split())

d =  obed(n0, pric0, 1)
print (d)
 


