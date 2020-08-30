
import sys

s = ''
i = 0
t_word = []
for word in sys.stdin:
	word_s = word.split()
	t_word.extend(word_s)

for line in t_word:
	#print (line)
	m_l = len(line)
	#print (m_l)
	if m_l>i:
		s = line
		i = m_l

print (s,i)
	



