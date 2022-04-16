from abc import ABC, abstractmethod


class TargetInterface(ABC):
	"""
	The Target defines the domain-specific interface used by the client code.
	"""
	@abstractmethod
	def request(self) -> str:
		pass


class Target(TargetInterface):
	"""
	The actual client code that implements the Target Interface
	"""
	def request(self) -> str:
		return "Target: The default target's behavior."


class Adaptee:
	"""
	The Adaptee contains some useful behavior, but its interface is incompatible
	with the existing client code. The Adaptee needs some adaptation before the
	client code can use it.
	"""

	def specific_request(self) -> str:
		return ".eetpadA eht fo roivaheb laicepS"


class Adapter(TargetInterface):
	"""
	The Adapter makes the Adaptee's interface compatible with the Target's
	interface via composition.
	"""

	def __init__(self, adaptee: Adaptee) -> None:
		self.adaptee = adaptee

	def request(self) -> str:
		return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


def client_code(target: Target) -> None:
	"""
	The client code supports all classes that follow the Target interface.
	"""

	print(target.request())


if __name__ == "__main__":
	print("Client: I can work just fine with the Target objects:")
	target = Target()
	client_code(target)
	print()

	adaptee = Adaptee()
	print("Client: The Adaptee class has a weird interface. See, I don't understand it:")
	print(f"Adaptee: {adaptee.specific_request()}")
	print()

	print("Client: But I can work with it via the Adapter:")
	adapter = Adapter(adaptee)
	client_code(adapter)
