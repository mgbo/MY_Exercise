def ticket(n):
	remin=0
	while n>0 :
		remin=remin*10+n%10
		#remin=n%10
		n=n/10
	return remin
	

a=int(raw_input())
ans=ticket(a)
print ans
