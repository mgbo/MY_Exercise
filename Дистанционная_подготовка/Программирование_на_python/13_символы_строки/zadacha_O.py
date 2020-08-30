
n = input()

def LongestWord(s):

	words = s.split()
	print (words) # list
	id_longest = 0

	for i in range(1, len(words)):

		if '.' in words[i]:
			words[i] = words[i].replace('.','')
			# print (words[i])

		if len(words[id_longest]) < len(words[i]):
			id_longest = i

	return words[id_longest]

ans = LongestWord(n)
print (ans)