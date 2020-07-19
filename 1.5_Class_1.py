class MoneyBox:
	def __init__(self, capaсity = 1000):
		self.capaсity = capaсity
		self.quantity = 0
	def can_add(self, v):
		if (self.quantity + v) > self.capaсity:
			return False
		else: 
			return True
	def add(self, v):
		if self.can_add(v):
			self.quantity += v
		else:
			return False






























