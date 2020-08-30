

n = int(input())

new = []
for i in range(n):
	d,m,y = map(str,input().split('/'))
	new.append((d,m,y))

#print (new)

def date_sort(d):
	d,m,y = d
	return y,m,d
	
ans = sorted(new,key=date_sort)
#print (ans)

'''
for i in ans:
	print ("{2}/{1}/{0}".format(i[0],i[1],i[2]))
'''
for i in ans:
	s = '/'.join(i)
	print (s)

print (s)








