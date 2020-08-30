
f = open("input_F.txt",'r')

word = set()
for w in f:
 	word.update(w.split())

print (len(word))
f.close()
