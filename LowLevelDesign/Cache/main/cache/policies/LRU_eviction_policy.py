from algorithms.doubly_linked_list import DoublyLinkedList
from cache.policies.eviction_policy import EvictionPolicy


class LRUEvictionPolicy(EvictionPolicy):
	def __init__(self) -> None:
		"""
			initialize doubley linked list
		"""
		self.dll = DoublyLinkedList()
		self.mapper = {}

	def key_accessed(self, key):
		"""
			keep moving the recently accessed key to the end 
			Kepping the most recently used keys in the end
		"""
		if key in self.mapper:
			self.dll.detach_node(self.mapper.get(key))
			self.dll.add_node_at_last(self.mapper.get(key))
		else:
			new_node = self.dll.add_element_at_last(key)
			self.mapper[key] = new_node
	
	def evict_key(self):
		"""
			purge the least recently used key from linked list
			least recently used key is in start of linked list
		"""
		first = self.dll.get_first_node()
		if not first:
			return None
		self.dll.detach_node(first)
		return first.element
