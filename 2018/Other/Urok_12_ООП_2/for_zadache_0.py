


worker_list = [4,4,1,4,4]

def check(worker_list):
	first_worker = worker_list[0]
	for i in worker_list[1:]:
		print (first_worker, i)
		if first_worker != i:
			return (-1111)
	return 1111

print (check(worker_list))


# ------------ vrain 1 -------------
def Round(w_l):

	last_w = w_l[0]
	print ("last worker : ",last_w)
	koliche = len(w_l)
	
	for i in range (koliche):
		next_w = w_l[(koliche+(i+1))%koliche]
		w_l[(koliche+(i+1))%koliche] = last_w
		last_w = next_w
		print (last_w)

l = [1,3,5,6,8,6,8]
Round(l)

def Round_1(w_l):
	for i in range(len(w_l)-1):
		w_l[i], w_l[(i+1)%len(w_l)] = w_l[(i+1)%len(w_l)], w_l[i]
		print (w_l)

#Round_1(l)
#print (l)





