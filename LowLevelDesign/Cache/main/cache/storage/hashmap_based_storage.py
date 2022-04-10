from cache.exceptions.not_found_exception import NotFoundException
from cache.exceptions.storage_full_exception import StorageFullException
from cache.storage.storage import Storage


class HashMapBasedStorage(Storage):
	def __init__(self, capacity) -> None:
		self.capacity = capacity
		self.storage = {}		# python hashmap

	def is_storage_full(self):
		return len(self.storage) == self.capacity

	def add(self, key, value):
		"""
			add the key to storage and assign a value
			if the key is alredy existing then updates the value
		"""
		if self.is_storage_full():
			raise StorageFullException("Capacity Full")
		self.storage[key] = value
	
	def remove(self, key):
		"""
			remove the key from storage 
			throw exception if key not found
		"""
		if key not in self.storage:
			raise NotFoundException(f"{key} do not exists in cache")
		del self.storage[key]

	def get(self, key):
		"""
			return the value for key, raise exception if not found
		"""
		if key not in self.storage:
			raise NotFoundException(f"{key} dosen't exist in cache")
		return self.storage.get(key)
