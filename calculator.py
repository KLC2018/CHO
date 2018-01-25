class Calculator():
	def __init__(self,list):
		self.list=list

	def sum(self):
		self.num=0
		for i in self.list:
			self.num+=i
		return self.num

	def avg(self):
		self.count=len(self.list)
		return self.num/self.count

