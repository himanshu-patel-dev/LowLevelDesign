from abc import ABC, abstractmethod


class EvictionPolicy(ABC):
	"""
		Interface or Abstract class for defining eviction policies
	"""
	
	@abstractmethod
	def key_accessed(self, key):
		pass

	@abstractmethod
	def evict_key(self):
		pass