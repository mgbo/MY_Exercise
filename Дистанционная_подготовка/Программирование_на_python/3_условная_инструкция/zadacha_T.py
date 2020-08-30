

n = int(input())
list_ticket = []


if n >= 60:
	list_ticket.append(n//60)
	n = n%60
else:
	list_ticket.append(0)


if n>=10:
	list_ticket.append(n//10)
	n = n%10
else:
	list_ticket.append(0)


if n>0:
	list_ticket.append(n)
else:
	list_ticket.append(0)

print (*(list_ticket[::-1]))




