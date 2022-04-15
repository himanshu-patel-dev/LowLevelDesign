from abc import ABC, abstractmethod


class Chair(ABC):
	"""
	Chair abstract product
	"""
	@abstractmethod
	def sit_on(self):
		pass


class Sofa(ABC):
	"""
	Abstract Sofa product
	"""
	@abstractmethod
	def sleep_on(self):
		pass
