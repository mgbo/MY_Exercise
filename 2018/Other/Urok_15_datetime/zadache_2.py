
import datetime
import time


with open('bet.log','r') as f, open('output.txt','w') as fout:
    for ss in f:
        s = ss.split()
        t = int(s[0])

        # date1 = datetime.datetime.fromtimestamp(t)
        # print (date1)

        time1 = time.strftime("%H:%M", time.gmtime(t))
        #print (time1)

        print (time1, file=fout)

f.close()

#------------------------------------------------------------------------

t = datetime.date.today()
print (t)





