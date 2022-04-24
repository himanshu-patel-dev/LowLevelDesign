from mediator import Mediator


class BaseComponent:
	"""
	The Base Component provides the basic functionality of storing a mediator's
	instance inside component objects.
	"""

	def __init__(self, mediator: Mediator = None) -> None:
		self._mediator = mediator

	@property
	def mediator(self) -> Mediator:
		return self._mediator

	@mediator.setter
	def mediator(self, mediator: Mediator) -> None:
		self._mediator = mediator

"""
Concrete Components implement various functionality. They don't depend on other
components. They also don't depend on any concrete mediator classes.
"""

class Component1(BaseComponent):
	def do_a(self) -> None:
		print("Component 1 does A.")
		self.mediator.notify(self, "A")

	def do_b(self) -> None:
		print("Component 1 does B.")
		self.mediator.notify(self, "B")

class Component2(BaseComponent):
	def do_c(self) -> None:
		print("Component 2 does C.")
		self.mediator.notify(self, "C")

	def do_d(self) -> None:
		print("Component 2 does D.")
		self.mediator.notify(self, "D")

