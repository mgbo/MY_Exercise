
def ticket(n, remin):
	remin=remin*10+n%10
	#remin=n%10
	n=n/10
	#print '%d %d\n'%(n, remin)
	return n, remin
	
def revers(n) :
	n, rem = ticket(n, 0)
	n, rem = ticket(n, rem)
	n, rem = ticket(n, rem)
	n, rem = ticket(n, rem)
	n, rem = ticket(n, rem)
	n, rem = ticket(n, rem)
	return rem
	
a=int(raw_input())
ans =revers(a)
print ans
