
import datetime
import time

f = open('bet.log','r')

t = []
for ss in f:
	if not f:
		break
	s = ss.split()

	vyemye = s[0]

	t.append(vyemye)

fir_vyemye = int(t[0]) # начальная дата
fin_vyemye = int(t[-1]) # последная дата

print ('начальная дата в секунде : ',fir_vyemye)
print ('последная дата в секунде : ',fin_vyemye)

res = fin_vyemye - fir_vyemye
print ('Разница между начальными и последными времени :',res)

date1 = datetime.datetime.fromtimestamp(fir_vyemye)
print (date1)

ans = datetime.timedelta(seconds=res) # превращает с секунда к часу и минутам
print ('в часах и минутах и секундах : ',ans) # длительность в часах и минутах и секундах

one_day = datetime.timedelta(days=1)
date2 = datetime.datetime.fromtimestamp(fin_vyemye) + one_day

print (date2)
print(date2 - date1)

ans = datetime.timedelta(seconds=res)
print (ans)

