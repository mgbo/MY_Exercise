
f = open('bet.log','r')

vremya = []

for line in f:
	sec, client, tik =line.split()
	vremya.append(sec)

f_vermya=vremya[0]
final_vermya=vremya[-1]


f.close()
