import datetime

# it maintains a dictionary maintaining a single state for all instances
class MonoState:
	_state = {}

	def __new__(cls, *args, **kwargs):
		# create a new instance
		self = super().__new__(cls)	
		# new instance have same properties as prev instance
		self.__dict__ = cls._state
		# return new instance
		return self

# from singleton_monostate import MonoState

class Logger(MonoState):
	log_file = None

	# need for open file method is removed
	def __init__(self, path):
		if not self.log_file:
			self.log_file = open(path, 'w')

	def write_log(self, log_record):
		now = datetime.datetime.now().strftime("%m-%d-%Y, %H:%M:%S")
		record = f"{now}: {log_record}"
		self.log_file.writelines(record)

	def close_log(self):
		if self.log_file:
			self.log_file.close()
			self.log_file = None


logger1 = Logger('MyLog4.log')
logger1.write_log('First Line of log')
logger2 = Logger('MyLog4_2.log')
logger2.write_log('Second Line of log')
logger1.close_log()
logger2.close_log()


with open('MyLog4.log', 'r') as log:
	for line in log:
		print(line)
