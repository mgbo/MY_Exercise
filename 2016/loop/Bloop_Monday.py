
(price,delta,day)=map(int,raw_input().split())

#day=m*7
i=1
money=0

#print i/7

while i<=day:
	print "money : ",money
	money=money+price
	if i/7!=0 and i%7==1:
		#print money
		money+=delta
		#delta+=delta
	i+=1
	
print "money : ",money
#print i-1
