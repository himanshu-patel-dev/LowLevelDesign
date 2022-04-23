from collections.abc import Iterator


"""
To create an iterator in Python, there are two abstract classes from the 
built-in `collections` module - Iterable and Iterator. We need to implement the
`__iter__()` method in the iterated object (collection), and the `__next__ ()`
method in the iterator.
"""
# when the collection object is called with iter() method then it return 
# Iterator object, thus to make AlphabeticalOrderIterator as Iterator we
# Inherited from Iterator 
class AlphabeticalOrderIterator(Iterator):
	"""
	Concrete Iterators implement various traversal algorithms. These classes
	store the current traversal position at all times.
	"""

	"""
	`_position` attribute stores the current traversal position. An iterator may
	have a lot of other fields for storing iteration state, especially when it
	is supposed to work with a particular kind of collection.
	"""
	_position: int = None

	"""
	This attribute indicates the traversal direction.
	"""
	_reverse: bool = False

	def __init__(self, collection, reverse: bool = False) -> None:
		self._collections = collection
		self._reverse = reverse
		self._position = -1 if reverse else 0		# deciding whether to start from front or back

	def __next__(self):
		"""
		The __next__() method must return the next item in the sequence. On
		reaching the end, and in subsequent calls, it must raise StopIteration.
		"""
		try:
			value = self._collections[self._position]		# fetch data at current index
			self._position += -1 if self._reverse else 1	# inc index if not reverse traversal else dec
		except IndexError:
			raise StopIteration()

		return value