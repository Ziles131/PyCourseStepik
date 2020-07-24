class ExtendedStack(list):
	'''def append(self, x):
		c = super(ExtendedStack, self).append(x)
		return c'''
	def pop(self):
		v = super(ExtendedStack, self).pop()
		return v

	def sum(self):
		if len(self) >= 2:
			return self.append(self.pop() + self.pop())
		else:
			return
	def sub(self):
		if len(self) >= 2:
			return self.append(self.pop() - self.pop())
		else:
			return
	def mul(self):
		if len(self) >= 2:
			return self.append(self.pop() * self.pop())
		else:
			return
	def div(self):
		if len(self) >= 2:
			return self.append(self.pop() // self.pop())
		else:
			return

