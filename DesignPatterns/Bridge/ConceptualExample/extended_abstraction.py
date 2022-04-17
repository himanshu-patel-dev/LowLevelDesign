from abstraction import Abstraction


class ExtendedAbstraction(Abstraction):
	"""
	You can extend the Abstraction without changing the Implementation classes.
	"""
	def operation(self) -> str:
		return (f"ExtendedAbstraction: Extended operation with:\n"
			f"{self.implementation.operation_implementation()}")
