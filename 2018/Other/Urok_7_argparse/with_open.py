
i = [str(i)+str(i-1) for i in range(20)]
print (i)

with open ('text.txt','w') as f:
	for index in i:
		f.write(index+'\n')
