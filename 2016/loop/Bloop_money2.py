
(price,delta,m)=map(int,raw_input().split())


day=m*7
i=1
week_day = 1
week_day2=1
money=0

while i<=day:
	
	money=money+price
	print "i=%d money=%d"% (i, money)
	i=i+1
	week_day += 1
	week_day2+= 1
	print "money=%d week_day=%d week_day2=%d" % (money,week_day,week_day2)
	if week_day == 8:
		price+=delta
		week_day = 1
		print "price=%d "% price
	
		#price-=1
	if week_day2==9:
		week_day2=2
		price=price-delta
		print "price(2)=%d "% price
		
print money
print i-1
