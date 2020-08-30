

s, n = map(int, input().split())

dannyye = [int(input()) for i in range(n)]

# print (s, n)
# print (dannyye)

sumUser = 0
play_capacity = 0

dannyye.sort()

for d in dannyye:
	if sumUser < s:
		sumUser += d
		if sumUser < s:
			play_capacity += 1
			# print ("sumUser : {} ,play_capacity : {}".format(sumUser,play_capacity))

print (play_capacity)

