
import sys

s = ''
i = 0
for word in sys.stdin.read().split():
	print (word)
	#print (type(word))
	m_l = len(word)
	print (m_l)
	#print (m_l)
	if m_l>i:
		s = word
		i = m_l

print (s,i)







