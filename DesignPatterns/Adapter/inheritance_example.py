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

# the method are inherited from left to right
# request from Target will be inherited in Adapter first and then specific_request from Adaptee
# in case we have two method with same name the method from the first class (Target here) will
# be the one which is used in Adapter
class Adapter(TargetInterface, Adaptee):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via multiple inheritance.
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: Target) -> None:
    """
    The client code supports all classes that follow the Target interface.
    """
    print(target.request())


if __name__ == "__main__":
	print("Client: I can work just fine with Target objects:")
	target = Target()
	client_code(target)
	print()

	adaptee = Adaptee()
	print("Client: The Adaptee class has a weird interface. See, I don't understand it:")
	print(f"Adaptee: {adaptee.specific_request()}")
	print()

	print("Client: But I can work with it via the Adapter:")
	adapter = Adapter()
	client_code(adapter)
