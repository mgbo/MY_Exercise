
def cal_2(n):
	for i in n:
		if i == "*":
			nn = n.split(i)
			ans = int(nn[0]) * int(nn[1])
			print (nn)
			return ans

		elif i == "+":
			nn = n.split(i)
			ans = int(nn[0]) + int(nn[1])
			print (nn)
			return ans

		elif i == "-":
			nn = n.split(i)
			ans = int(nn[0]) - int(nn[1])
			print (nn)
			return ans


n = input()
ans = cal_2(n)
print (ans)




