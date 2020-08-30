
def count_letters(word):
    return len(word) - word.count(' ') - word.count('.') - word.count('\n')

def count_words(word):
	return len(word)

with open('file_J.txt', 'r') as f:
	total_letter = 0
	total_words = 0
	total_line = 0

	for l in f:
		#---------- for letters numbers -----------
		num = count_letters(l)
		#print (num)
		total_letter +=num
		#print (total_letter)

		#--------- for words numbers ----------
		num_w = count_words(l.split())
		total_words+=num_w
		#print (total_words)

		# ------ for line numbers ----------
		total_line +=1
		#print (total_line)

f.close()

print ("Input file contains:")
print ("{} letters ".format(total_letter))
print ("{} words ".format(total_words))
print ("{} lines ".format(total_line))


