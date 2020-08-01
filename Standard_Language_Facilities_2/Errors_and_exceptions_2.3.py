class NonPositiveError(Exception):
	pass
class PositiveList(list):
	def append(self, x):
		if int(x) > 0:
			y = super(PositiveList, self).append(x)
			return y
		else:
			raise NonPositiveError("incorrect number")