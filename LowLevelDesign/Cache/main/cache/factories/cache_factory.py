from cache.cache import Cache
from cache.policies.LRU_eviction_policy import LRUEvictionPolicy
from cache.storage.hashmap_based_storage import HashMapBasedStorage


class CacheFactory:	
	def default_cache(self, capacity):
		storage = HashMapBasedStorage(capacity)
		policy = LRUEvictionPolicy()
		return Cache(policy, storage)
