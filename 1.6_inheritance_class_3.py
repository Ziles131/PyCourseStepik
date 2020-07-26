import time

class Loggable:
	def log(self, msg):
		print(str(time.ctime()) + ": " + str(msg))
		
class LoggableList(list, Loggable):
	def append(self, v):
		super(LoggableList, self).append(v)
		super(LoggableList, self).log(v)

l = LoggableList()
print(l)
l.append(17)
l.append(1)
l.append(89)
l.append(9)
l.append(35)
