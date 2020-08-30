
alpha = 'abcdefghijklmnopqrstuvwxyz'
print (alpha)

def Cipher(my_word, n):
	code =''
	for letter in my_word:
		if letter !=' ':
			code+=alpha[((alpha.index(letter.lower()))+n)%len(alpha)]
		else:
			code+=' '
	return code


ans = Cipher('abcdefghijklmnopqrstuvwxyz',3)
print ("ans : ",ans)

n = 0


with open('file_K.txt', 'r') as f:

	for letter in f:
		l_s = letter.strip()
		#print (l_s)

		n+=1
		#print (n)

		my_code = Cipher(l_s,n)
		print (my_code)


f.close()
