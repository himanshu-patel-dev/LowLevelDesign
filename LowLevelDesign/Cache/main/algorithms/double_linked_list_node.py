class DoubleLinkedListNode:
	"""
		Node of a double linked list
	"""
	def __init__(self, element) -> None:
		self.next = None
		self.prev = None
		self.element = element
