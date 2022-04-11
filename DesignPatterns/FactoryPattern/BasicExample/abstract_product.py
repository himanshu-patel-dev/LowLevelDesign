from abc import ABC, abstractmethod

class Product(ABC):
	"""
    The Product interface declares the operations that all concrete products
    must implement.
    """
	
	@abstractmethod
	def operations(self):
		pass
