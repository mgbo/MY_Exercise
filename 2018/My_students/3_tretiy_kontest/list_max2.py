
import sys

new_list = []

for line in sys.stdin:
	mm = list(map(int,line.split()))
	#print (mm)
	new_list+=mm
	min_n = min(new_list)
	min_max = max(new_list)


print (min_n)
print (min_max)
