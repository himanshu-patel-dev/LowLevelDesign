from abstraction import Abstraction
from extended_abstraction import ExtendedAbstraction
from concrete_implementation import ConcreteImplementationA, ConcreteImplementationB

def client_code(abstraction: Abstraction)-> None:
	"""
	Except for the initialization phase, where an Abstraction object gets linked
	with a specific Implementation object, the client code should only depend on
	the Abstraction class. This way the client code can support any abstraction-
	implementation combination.
	"""
	print(abstraction.operation())


if __name__ == "__main__":
	"""
	The client code should be able to work with any pre-configured abstraction-
	implementation combination.
	"""
	implementation = ConcreteImplementationA()
	abstraction = Abstraction(implementation)
	client_code(abstraction)

	print()

	implementation = ConcreteImplementationB()
	abstraction = ExtendedAbstraction(implementation)
	client_code(abstraction)
