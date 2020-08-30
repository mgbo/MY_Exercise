
import sys

d = dict()
with open ('my_dict.txt', 'r') as f:
	for line in f:
		if not line:
			break
		w = line.split('-')
		en_w = w[0].strip()
		ru_w = w[1].strip()

		if en_w not in d:
			d[en_w] = ru_w

# for k,v in d.items():
# 	print (k,v)

print (d)

with open ('input_tran.txt', 'r') as f1, open('tran.txt','w') as fout:
	for w in f1:
		l_input = w.split()
		# print (l_input)
		for i in l_input:
			j = i.lower()
			# print (j)
			for k,v in d.items():
				if str(j) in k:
					# pass
					print (i, v)



f.close()
f1.close()
fout.close()









