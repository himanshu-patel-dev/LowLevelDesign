from collections.abc import Iterable
from typing import Any, List
from iterator import AlphabeticalOrderIterator


class WordsCollection(Iterable):
	"""
	Concrete Collections provide one or several methods for retrieving fresh
	iterator instances, compatible with the collection class.
	"""

	def __init__(self, collections: List[Any] = []) -> None:
		self._collection = collections

	def __iter__(self) -> AlphabeticalOrderIterator:
		"""
		The __iter__() method returns the iterator object itself, by default we
		return the iterator in ascending order.
		"""
		return AlphabeticalOrderIterator(self._collection)

	def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
		return AlphabeticalOrderIterator(self._collection, True)

	def add_item(self, item: Any):
		self._collection.append(item)
