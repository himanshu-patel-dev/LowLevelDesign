from abc import ABC, abstractmethod


class State(ABC):
	"""
	The base State class declares methods that all Concrete State should
	implement and also provides a backreference to the Context object,
	associated with the State. This backreference can be used by States to
	transition the Context to another State.
	"""
	@property
	def context(self):
		return self._context

	@context.setter
	def context(self, context):
		self._context = context

	@abstractmethod
	def handle1(self) -> None:
		pass

	@abstractmethod
	def handle2(self) -> None:
		pass

"""
Concrete States implement various behaviors, associated with a state of the Context.
"""

class ConcreteStateA(State):
	def handle1(self) -> None:
		print("ConcreteStateA handles request1.")
		print("ConcreteStateA wants to change the state of the context.")
		self.context.transition_to(ConcreteStateB())

	def handle2(self) -> None:
		print("ConcreteStateA handles request2.")


class ConcreteStateB(State):
	def handle1(self) -> None:
		print("ConcreteStateB handles request1.")

	def handle2(self) -> None:
		print("ConcreteStateB handles request2.")
		print("ConcreteStateB wants to change the state of the context.")
		self.context.transition_to(ConcreteStateA())
