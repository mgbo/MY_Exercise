
fin = open('test1.txt','r')
fout = open('output.txt','w')

for i in fin:
	print (i, file=fout)

fin.close()
fout.close()