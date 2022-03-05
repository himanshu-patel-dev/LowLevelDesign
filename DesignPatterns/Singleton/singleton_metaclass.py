import datetime

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

# from singleton_metaclass import Singleton

class Logger(metaclass=Singleton):
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


logger1 = Logger('MyLog3.log')
logger1.write_log('First Line of log')
logger2 = Logger('SameLogFile.log')
logger2.write_log('Second Line of log')
logger1.close_log()
logger2.close_log()


with open('MyLog3.log', 'r') as log:
	for line in log:
		print(line)
