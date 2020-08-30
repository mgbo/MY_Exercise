
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





'''

sn = list(map(int, input().split()))
s = sn[0] 
n = sn[1] 
t = [] 

numUser = 0 
sumUser = 0
pukUser = 0

while numUser < n:
	vUser = int(input()) 
	numUser += 1 
	t.append(vUser)
t.sort() 
# print (numUser, t)


for i in t:
	# print ('i --> {}'.format(i))

	if sumUser < s: 
		print (sumUser, s)
		sumUser += i 
		if sumUser < s: 
			pukUser += 1 
print(pukUser)

'''


