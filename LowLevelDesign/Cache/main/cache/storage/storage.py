from cache.exceptions.not_found_exception import NotFoundException
from cache.exceptions.storage_full_exception import StorageFullException
from abc import ABC, abstractmethod


class Storage(ABC):		
	@abstractmethod
	def add(self, key, value):
		raise StorageFullException

	@abstractmethod
	def remove(self, key):
		pass

	@abstractmethod
	def get(self, key):
		pass
