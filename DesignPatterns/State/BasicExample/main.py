from context import Context
from state import ConcreteStateA


if __name__ == "__main__":
	# The client code.

	context = Context(ConcreteStateA())
	context.request1()
	print('---')
	context.request2()
