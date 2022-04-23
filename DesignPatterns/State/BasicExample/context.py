from state import State


class Context:
	"""
	The Context defines the interface of interest to clients. It also maintains
	a reference to an instance of a State subclass, which represents the current
	state of the Context.
	"""
	_state = None
	"""
	A reference to the current state of the Context.
	"""

	def __init__(self, state: State) -> None:
		self.transition_to(state)

	def transition_to(self, state: State) -> None:
		"""
		The Context allows changing the State object at runtime.
		"""
		print(f"Context: Transition to {type(state).__name__}")
		self._state = state				# transition to the said state
		self._state.context = self		# back link the new state to current context

	"""
	The Context delegates part of its behavior to the current State object.
	"""

	def request1(self):
		self._state.handle1()

	def request2(self):
		self._state.handle2()
