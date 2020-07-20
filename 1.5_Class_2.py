class Buffer:
	def __init__(self):
		self.inlist = []
		# constructor with no arguments
	def add(self, *a):
		if len(self.inlist) < 5:
			self.inlist += list(a)
		while len(self.inlist) >= 5:
			self.x = 0
			for i in range(5):
				self.x += self.inlist[0]
				self.inlist.remove(self.inlist[0])
			print(self.x)
		# add the next part of the sequence
	def get_current_part(self):
		return self.inlist
		# return the currently saved sequence elements in order,
		# where they were added

