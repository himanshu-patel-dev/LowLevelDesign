from abc import ABC, abstractmethod


class Mediator(ABC):
	"""
	The Mediator interface declares a method used by components to notify the
	mediator about various events. The Mediator may react to these events and
	pass the execution to other components.
	"""
	@abstractmethod
	def notify(self, sender: object, event: str) -> None:
		pass


class ConcreteMediator(Mediator):
	def __init__(self, component1, component2) -> None:
		self._component1 = component1
		self._component1.mediator = self
		self._component2 = component2
		self._component2.mediator = self
	
	def notify(self, sender: object, event: str) -> None:
		if event == "A":
			print("Mediator reacts on A and triggers following operations:")
			self._component2.do_c()
		elif event == "D":
			self._component1.do_b()
			self._component2.do_c()
