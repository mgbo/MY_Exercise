
text = input()
# text.lower()


vowels = 'aeiouy'

def remove_vowels(vowels, text):
	ans = ''
	for t in text:
		if t not in vowels:
			ans += t
	return ans

res = remove_vowels(vowels, text)
print (res)

