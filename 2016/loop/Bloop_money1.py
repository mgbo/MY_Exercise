
(price,delta,m)=map(int,raw_input().split())


day=m*7
i=0
money=0

while i<day:
	money=money+price
	price=price+delta
	i=i+1
	

print money
