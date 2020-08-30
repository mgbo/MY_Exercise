
n = int(input())

def input_ret():
	rect = []
	for i in range(n):
		rect.append(list(map(int,input().split())))
	return rect

Ret = input_ret()

f_ret_x = Ret[0][0]
#print ("x for first Rectangle : ",f_ret_x)

count = 0
for r in Ret[1:]:
	xrb_other = r[2]
	#print (xrb_other)

	if xrb_other<f_ret_x:
		count+=1

print (count)



