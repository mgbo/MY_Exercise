
import sys
list_new_min = []
list_new_max = []

for line in sys.stdin:
	mm = list(map(int,line.split()))
	
	min_n = min(mm)
	list_new_min.append(min_n)

	max_n = max(mm)
	list_new_max.append(max_n)

#print ("только минимальные число из строки : ",list_new_min)
min_nn = min(list_new_min)
print (min_nn)
print (max(list_new_max))