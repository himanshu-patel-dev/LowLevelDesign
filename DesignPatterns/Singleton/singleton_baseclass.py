import datetime

class Singleton:
	_instances = {}		# dict([cls, instance])

	def __new__(cls, *args, **kwargs):
		if cls not in cls._instances:
			instance = super().__new__(cls)
			cls._instances[cls] = instance
		return cls._instances[cls]

# from singleton_baseclass import Singleton

class Logger(Singleton):
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


logger1 = Logger('MyLog2.log')		# need for Logger.instance() is removed
logger1.write_log('First Line of log')
logger2 = Logger('SameLogFile.log')
logger2.write_log('Second Line of log')
logger1.close_log()
logger2.close_log()


with open('MyLog2.log', 'r') as log:
	for line in log:
		print(line)
