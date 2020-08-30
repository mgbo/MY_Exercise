
a = int(input())
b = int(input())


ans = (-b)/a 

ans_1 = int(ans)


if ans_1 == ans:
	print (ans_1)

elif a==0 or b==0:
	print ('INF')

elif ans==0:
	print ("NO")