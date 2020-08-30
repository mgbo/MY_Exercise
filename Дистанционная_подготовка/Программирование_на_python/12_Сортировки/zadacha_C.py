

def input_chisel():
	result = [0,0,0,0,0,0,0,0,0]
	n = ''
	while n!=0:
		n = int(input())

		if n == 1:
			result[n-1] += 1 

		elif n == 2:
			result[n-1] += 1 

		elif n == 3:
			result[n-1] += 1 

		elif n == 4:
			result[n-1] += 1 

		elif n == 5:
			result[n-1] += 1 

		elif n == 6:
			result[n-1] += 1 

		elif n == 7:
			result[n-1] += 1

		elif n == 8:
			result[n-1] += 1 

		elif n == 9:
			result[n-1] += 1  

	return result

ans = input_chisel()
print (*ans)






