import datetime

class Logger:
	log_file = None

	@staticmethod
	def instance():
		if '_instance' not in Logger.__dict__:
			Logger._instance = Logger()
		return Logger._instance

	def open_log(self, path):
		self.log_file = open(path, mode='w')
		self.log_file.writelines('\n')

	def write_log(self, log_record):
		now = str(datetime.datetime.now().strftime("%m-%d-%Y, %H:%M:%S"))
		record = f"{now}: {log_record}"
		self.log_file.writelines(record)
	
	def close_log(self):
		self.log_file.close()


logger = Logger.instance()
logger.open_log('MyLog.log')
logger.write_log('Logger with classic Singleton pattern')
logger.close_log()

with open('MyLog.log', 'r') as log:
	for line in log:
		print(line)
