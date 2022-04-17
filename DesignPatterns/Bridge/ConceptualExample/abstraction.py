from abstract_implementation import Implementation


class Abstraction:
	"""
	The Abstraction defines the interface for the "control" 
	part of the two class hierarchies. It maintains a reference to 
	an object of the Implementation hierarchy and delegates all of the real work to this object.
	Abstraction is not a abstract class.
	"""

	def __init__(self, implementation: Implementation) -> None:
		self.implementation = implementation

	def operation(self) -> str:
		return (f"Abstraction: Base operation with:\n"
				f"{self.implementation.operation_implementation()}")
