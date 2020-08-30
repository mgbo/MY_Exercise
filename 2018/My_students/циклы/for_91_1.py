
r,c = map(int,input().split())

for row in range(r):
		if row==0 or row==r-1:
			print ("*"*c)
		else:
			if c == 1:
				print('*')
			else:
				print ('*'+" "*(c-2)+'*')

