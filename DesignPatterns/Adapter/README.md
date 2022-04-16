# Adapter Pattern

# Intent
Adapter is a structural design pattern that allows objects with incompatible interfaces to collaborate.

The Adapter acts as a wrapper between two objects. It catches calls for one object and transforms them to format and interface recognizable by the second object.

## Identification
Adapter is recognizable by a constructor which takes an instance of a different abstract/interface type. When the adapter receives a call to any of its methods, it translates parameters to the appropriate format and then directs the call to one or several methods of the wrapped object.

## Conceptual Example (via inheritance)

```python
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
class Adapter(Target, Adaptee):
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
```
```bash
Client: I can work just fine with Target objects:
Target: The default target's behavior.

Client: The Adaptee class has a weird interface. See, I don't understand it:
Adaptee: .eetpadA eht fo roivaheb laicepS

Client: But I can work with it via the Adapter:
Adapter: (TRANSLATED) Special behavior of the Adaptee.
```

## Conceptual Example (via object composition)

```python
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
```
```bash
Client: I can work just fine with the Target objects:
Target: The default target's behavior.

Client: The Adaptee class has a weird interface. See, I don't understand it:
Adaptee: .eetpadA eht fo roivaheb laicepS

Client: But I can work with it via the Adapter:
Adapter: (TRANSLATED) Special behavior of the Adaptee.
```

## Structure

### Class adapter - via inheritance

This implementation uses inheritance: the adapter inherits interfaces from both objects at the same time. Note that this approach can only be implemented in programming languages that support multiple inheritance, such as C++.

The Class Adapter doesn’t need to wrap any objects because it inherits behaviors from both the client and the service. The adaptation happens within the overridden methods. The resulting adapter can be used in place of an existing client class.

### Object adapter - via object composition

- The Client is a class that contains the existing business logic of the program.
- The Client Interface describes a protocol that other classes must follow to be able to collaborate with the client code.
- The Service is some useful class (usually 3rd-party or legacy). The client can’t use this class directly because it has an incompatible interface.
- The Adapter is a class that’s able to work with both the client and the service: it implements the client interface, while wrapping the service object. The adapter receives calls from the client via the adapter interface and translates them into calls to the wrapped service object in a format it can understand.
- The client code doesn’t get coupled to the concrete adapter class as long as it works with the adapter via the client interface. Thanks to this, you can introduce new types of adapters into the program without breaking the existing client code. This can be useful when the interface of the service class gets changed or replaced: you can just create a new adapter class without changing the client code.

## Applicability
- Use the Adapter class when you want to use some existing class, but its interface isn’t compatible with the rest of your code.
- Use the pattern when you want to reuse several existing subclasses that lack some common functionality that can’t be added to the superclass.

## Pros and Cons

### Pros
- Single Responsibility Principle. You can separate the interface or data conversion code from the primary business logic of the program.
- Open/Closed Principle. You can introduce new types of adapters into the program without breaking the existing client code, as long as they work with the adapters through the client interface.
### Cons
- The overall complexity of the code increases because you need to introduce a set of new interfaces and classes. Sometimes it’s simpler just to change the service class so that it matches the rest of your code.

## How to Implement
1. Make sure that you have at least two classes with incompatible interfaces:
	- A useful service class, which you can’t change (often 3rd-party, legacy or with lots of existing dependencies).
	- One or several client classes that would benefit from using the service class.
	Declare the client interface and describe how clients communicate with the service.
2. Create the adapter class and make it follow the client interface. Leave all the methods empty for now.
3. Add a field to the adapter class to store a reference to the service object. The common practice is to initialize this field via the constructor, but sometimes it’s more convenient to pass it to the adapter when calling its methods.
4. One by one, implement all methods of the client interface in the adapter class. The adapter should delegate most of the real work to the service object, handling only the interface or data format conversion.
5. Clients should use the adapter via the client interface. This will let you change or extend the adapters without affecting the client code.
