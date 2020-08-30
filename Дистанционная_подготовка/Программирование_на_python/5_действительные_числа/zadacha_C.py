
'''
Округление по российским правилам
'''

import math

x = float(input())

y = (x * 10 )%10
# print(y)


if y < 5:
	ans = int(x)

else:
	ans = math.ceil(x)

print (ans)



# n = float(input())

# # nn = math.ceil(n)
# nn = math.round(n)
# print (nn)