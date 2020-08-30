# -*- coding:utf-8 -*-
lis_name = []
lis_duration = []

with open('tr.log','r') as f:
	for line in f:
		s = line.split()
		nazvaniye = s[2]
		lis_name.append(nazvaniye)
DD = {}
for j in lis_name:
	DD[j] = DD.get(j,0)+1

for k,v in DD.items():
	print(k,v)
# ----------------------------------------
print ("---------------------------")

N = input()
with open('tr.log','r') as f:
	for line in f:
		s = line.split()
		if N == s[2]:
			dlitelna = s[3]
			lis_duration.append(dlitelna)
f.close()

# преобразовывать в float от str
lis_duration = [float(i) for i in lis_duration]
print (lis_duration)

for i in range(len(lis_duration)):
	print (lis_duration[i])
s_lis_dur= sum(lis_duration)
print ("total sum of X duraition : ",s_lis_dur)
print ("Средняя Длительность действия N :",s_lis_dur/len(lis_duration))
