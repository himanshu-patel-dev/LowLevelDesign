from multiprocessing.sharedctypes import Value
from threading import Lock, Thread
from tokenize import single_quoted

class SingletonMeta(type):
	"""
	This is a thread-safe implementation of Singleton.
	"""
	_instances = {}
	_lock = Lock()
	"""
	We now have a lock object that will be used to synchronize threads during
	first access to the Singleton.
	"""

	def __call__(cls, *args, **kwds):
		"""
		Possible changes to the value of the `__init__` argument do not affect
		the returned instance.

		Now, imagine that the program has just been launched. Since there's no
		Singleton instance yet, multiple threads can simultaneously pass the
		previous conditional and reach this point almost at the same time. The
		first of them will acquire lock and will proceed further, while the
		rest will wait here.        
		"""
		with cls._lock:		# acquiring lock at start of context manager and release on exit
			if cls not in cls._instances:
				cls._instances[cls] = super().__call__(*args, **kwds)
			return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
	value:str = None
	"""
	We'll use this property to prove that our Singleton really works.
	"""

	def __init__(self, value: str) -> None:
		self.value = value

	def business_logic(self):
		"""
		Finally, any singleton should define some business logic, which can be
		executed on its instance.
		"""

def test_singleton(value):
	"""
	This function is for thread
	"""
	singleton = Singleton(value)
	print(singleton.value)

if __name__ == "__main__":
	# The client code.

	print("If you see the same value, then singleton was reused (yay!)\n"
		  "If you see different values, "
		  "then 2 singletons were created (booo!!)\n\n"
		  "RESULT:\n")

	process1 = Thread(target=test_singleton, args=("FOO",))	# this , matters
	process2 = Thread(target=test_singleton, args=("BAR",))
	process1.start()
	process2.start()

# If you see the same value, then singleton was reused (yay!)
# If you see different values, then 2 singletons were created (booo!!)

# RESULT:

# FOO
# FOO