from algorithms.exceptions.invalid_element_exception import InvalidElementException
from algorithms.double_linked_list_node import DoubleLinkedListNode


class DoublyLinkedList:
	def __init__(self) -> None:
		"""
			Initialize two dummy node in Doubly Linked List
			and make them point to each other
		"""
		self.dummy_head = DoubleLinkedListNode(None)
		self.dummy_tail = DoubleLinkedListNode(None)

		self.dummy_head.next = self.dummy_tail
		self.dummy_tail.prev = self.dummy_head

	def detach_node(self, node):
		"""
			detach the given node from linked list
		"""
		if not node:
			return None
		
		node.prev.next = node.next
		node.next.prev = node.prev

	def add_node_at_last(self, node):
		"""
			Add the node passed to the end of linked list
		"""
		prev_node = self.dummy_tail
		prev_node.next = node
		node.prev = prev_node
		self.dummy_tail.prev = node
		node.next = self.dummy_tail

	def add_element_at_last(self, element):
		"""
			Add the element passed to the end of linked list
		"""
		if not element:
			raise InvalidElementException(f"Element is : {element}")

		new_node = DoubleLinkedListNode(element)
		self.add_node_at_last(new_node)
		return new_node

	def is_linked_list_blank(self):
		"""
			returns True if the linked list is blank else False
		"""
		return self.dummy_head.next == self.dummy_tail

	def get_first_node(self):
		"""
			return the first node of linked list
		"""
		if self.is_linked_list_blank():
			return None
		return self.dummy_head.next

	def get_last_node(self):
		"""
			returns last node of linked list
		"""
		if self.is_linked_list_blank():
			return None
		return self.dummy_tail.prev
