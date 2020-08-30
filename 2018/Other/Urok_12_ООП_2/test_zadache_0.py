
class Money():
	def __init__(self, rub=0):
		self.rub =rub

	def __str__(self):
		return 'я получил %d'%(self.rub)
	
	def __eq__(self, other):
		if self.rub == other.rub:
			return 1

	def __ne__(self, other):
		if self.rub != other.rub:
			return 0
	
	def __add__(self, other):
		self.rub +=other.rub
		return self

	def __sub__(self, other):
		return self.rub - other.rub
	

	def __truediv__(self, other):
		(self.rub) //other
		print ("rub : ",self.rub)
		return self

	def __div__(self, other):
		print ("div ", self.rub/other)
		return self.rub //other


	def __mul__(self, other):
		return self.rub*other


class Brigada():
	#brigada = [Money(5),Money(6),Money(7),Money(8),Money(10)]
	def __init__(self, worker_list = []):
		self.workers_tol = worker_list

	def __str__(self):
		s = ''
		for w in self.workers_tol:
			s = s + str(w) + '\n'
		s += '-----'
		return s

	def Round(self, worker_list):
		last_w = Money()
		next_w = Money()

		last_w = worker_list[0]
		#print ("last worker : ",last_w)

		koliche = len(worker_list)
		#print (koliche)

		for i in range (koliche):
			next_w = worker_list[(koliche+(i+1))%koliche]
			worker_list[(koliche+(i+1))%koliche] = last_w
			last_w = next_w
			#print (last_w)

	def getFrist(self, worker_list):
		return worker_list[0]

	def getSecond(self, worker_list):
		return worker_list[1]

	def putFirst(self, dengi):
		self.workers_tol[0] = dengi
		print ("First put :", self.workers_tol[0] )

	def putSecond(self,dengi):
		self.workers_tol[1] = dengi
		print ("Second put :", self.workers_tol[0] )


	def isEqual(self, worker_list):
		f_worker = worker_list[0]
		for wk in worker_list[1:]:
			#print (f_worker.rub,wk.rub)
			if f_worker.rub != wk.rub:
				return -1
		return 1
				
if __name__ == "__main__":

	worker_list = []
	
	a = Money() # for first worker
	b = Money() # for second worker
	c = Money()
	vladelets = Money() # for woner


	count_turn = 0 # how many turn

	# колечество работников
	for i in range(5):
		pitsan = int(input("Money for workers [{}] :".format(i+1))) 
		worker_list.append(Money(pitsan))

	workers = Brigada(worker_list)
	#print (workers)
	print ("===========")
	
	if workers.isEqual(worker_list)==1:
		print ("Справедливость!!!!")
	else:
		while(workers.isEqual(worker_list)!=1):

			print ("Before Turn : ")
			print (workers)

			workers.Round(worker_list)
			x = int(input("что нубудь : "))

			print ("\nAfter Turn : ")
			print (workers)

			a = workers.getFrist(worker_list)
			print ("First : ",a)

			b = workers.getSecond(worker_list)
			print ("Second : ",b)

			
			c = (a+b)
			print ("first + second : %s"%(c.rub))

			cc = c.rub//2
			print ("{} / {} = {}".format(c.rub,2,cc))
			
			count_turn +=1 # for count turn

			ppp = (c.rub -(cc*2))
			print ("владелец получит деньги для {} поворот : {}".format(count_turn,ppp))

			vladelets.rub += ppp
			print ("Vladelts : ", vladelets)
		

			total_a_b = Money(cc)

			workers.putFirst(total_a_b)
			
			workers.putSecond(total_a_b)

			print ("________________________")
			print (workers)
			
			

	print ("The number of turn is : ",count_turn)



