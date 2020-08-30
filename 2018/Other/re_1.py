
'''
import re

mytext = " mg aung, amayapuya city, machitthu@gmail.com"\
		"ma hla, bago city, dljfldjl@gmail.com"

textlookfor = "city"

result_all = re.findall(textlookfor,mytext)

print (result_all)

'''



worker_list = [4,4,1,4,4]


def check(worker_list):
	first_worker = worker_list[0]
	for i in worker_list[1:]:
		print (first_worker, i)
		if first_worker != i:
			return (-1111)
			#break
	return 1111


print (check(worker_list))















