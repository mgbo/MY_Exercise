
n = int(input())

num_participants = list(map(int, input().split()))
# print (num_participants)


d = {}

for i in num_participants:
	if i <= n:
		d[i] = d.get(i, 0) + 1

# print (d)

max_vote  = max(d.values())
# print (max_vote)


filter_winner = filter(lambda x: d[x] == max_vote, d.keys())
print (*filter_winner)



'''
def Golosovaniye(num_participants):
	result = []
	for i in set(num_participants):
		if i <= n:
			# print (i,num_participants.count(i))
			result.append([i,num_participants.count(i)])

	return result

def MyFn(s):
	return s[-1]

def ResultVoting(num_participants):
	total = Golosovaniye(num_participants)
	s_total = sorted(total, key=MyFn)
	print (s_total)


ResultVoting(num_participants)
'''

