
import sys
mm=0
mw=''
for line in sys.stdin:
	for s in line.split():
		#print s
		ss=len(s)
		#print ss
		if ss>mm:
				mm=ss
				mw = s

print ("%s %d")% (mw,mm) 		
