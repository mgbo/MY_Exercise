
class Turing():

	def __init__(self):
		
		self.rules={}
		self.ribbon=[]
		self.states=['0','fin'] ## ?????

	def maketuring(self,rulefilename):

		with open(rulefilename,'r') as f:
			s=[y.rstrip('\n') for y in f.readlines()]
			print(s)
			for x in s:
				print(x)
				xx= x.split('-')
				self.rules[tuple(xx[0].split(','))] = list(xx[1].split(','))
				
		
		
	def step(self):
		
		self.state = '0'
		i = 0 ##  сначала видит крайний левый символ
		while self.state != 'fin':
			temp=tuple([self.state,ribbon[i]])
			if temp in self.rules:
				self.state =  self.rules[temp][0]
				self.ribbon[i] = self.rules[temp][1]
				
				if self.rules[temp][2]=='r' : i+=1 # едет вправо
				elif  self.rules[temp][2] =='l' : i-=1 # едет влево
			#....................
			#....................
		
			else:
				
				raise KeyError("You deadlocked me, bloody bastard!")
				
#	def work(self):
#		while self.state != 'fin':
#			self.step()
