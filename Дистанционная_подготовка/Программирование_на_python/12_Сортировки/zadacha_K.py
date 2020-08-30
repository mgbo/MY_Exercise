
n = int(input())

list_infor = []

def input_data(n):
	
	for i in range(n):
		infor = input().split()
		print (infor)
		list_infor.append(infor)

	return list_infor


def MyFs(s):
	return s[-1]

def sort_data():
	result = []
	data_score = input_data(n)
	# print (data_score)
	new_sort = sorted(data_score, key=MyFs, reverse=True)
	# print (new_sort)
	for score in new_sort:
		print(score[0])

sort_data()
