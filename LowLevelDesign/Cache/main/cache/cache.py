from cache.exceptions.not_found_exception import NotFoundException
from cache.exceptions.storage_full_exception import StorageFullException
from cache.policies.eviction_policy import EvictionPolicy
from cache.storage.storage import Storage


class Cache:
	def __init__(self, eviction_policy: EvictionPolicy, storage: Storage) -> None:
		self.eviction_policy = eviction_policy
		self.storage = storage

	def put(self, key, value):
		try:
			self.storage.add(key, value)
			self.eviction_policy.key_accessed()
		except StorageFullException as e:
			print(f"Storage full will try to evict: {e}")
			key_to_remove = self.eviction_policy.evict_key()
			if not key_to_remove:
				raise Exception("Unexpected State. Storage full and no key to evict.")
			self.storage.remove(key_to_remove)
			print(f"Creating space by evicting item {key_to_remove}")
			self.put(key, value)

	def get(self, key):
		try:
			value = self.storage.get(key)
			self.eviction_policy.key_accessed(key)
			return value
		except NotFoundException as e:
			print(f"Tried to access non-existing key {e}")
			return None
