# Bridge Pattern

Bridge is a structural design pattern that divides business logic or huge class into separate class hierarchies that can be developed independently.

One of these hierarchies (often called the `Abstraction`) will get a reference to an object of the second hierarchy (`Implementation`). The abstraction will be able to delegate some (sometimes, most) of its calls to the implementations object. Since all implementations will have a common interface, they’d be interchangeable inside the abstraction.

Bridge can be recognized by a clear distinction between some controlling entity and several different platforms that it relies on.


## Problem 
Say you have a geometric `Shape` class with a pair of subclasses: `Circle` and `Square`. You want to extend this class hierarchy to incorporate colors, so you plan to create `Red` and `Blue` shape subclasses. However, since you already have two subclasses, you’ll need to create four class combinations such as `BlueCircle` and `RedSquare`.

<p style="text-align:center">
    <img src="../../static/shapes.png"/>
</p>

Adding new shape types and colors to the hierarchy will grow it exponentially. For example, to add a triangle shape you’d need to introduce two subclasses, one for each color. And after that, adding a new color would require creating three subclasses, one for each shape type. The further we go, the worse it becomes.

## Solution
This problem occurs because we’re trying to extend the shape classes in two independent dimensions: by `form` and by `color`. That’s a very common issue with class inheritance.

The Bridge pattern attempts to solve this problem by switching from `inheritance` to the `object composition`. What this means is that you extract one of the dimensions into a separate class hierarchy, so that the original classes will reference an object of the new hierarchy, instead of having all of its state and behaviors within one class.

<p style="text-align:center">
    <img src="../../static/shapes_referrence.png"/>
</p>

Following this approach, we can extract the color-related code into its own class with two subclasses: `Red` and `Blue`. The `Shape` class then gets a reference field pointing to one of the color objects. Now the shape can delegate any color-related work to the linked color object. That **reference** will act as a **bridge** between the `Shape` and `Color` classes. From now on, adding new colors won’t require changing the shape hierarchy, and vice versa.

#### Abstraction and Implementation
`Abstraction` (also called `interface`) is a high-level control layer for some entity. This layer isn’t supposed to do any real work on its own. It should delegate the work to the `implementation` layer (also called `platform`).
Note that we’re not talking about `interfaces` or `abstract` classes from your programming language. These aren’t the same things.

## Structure
<p style="text-align:center">
    <img src="../../static/bridge_structure.png"/>
</p>

- The `Abstraction` provides high-level control logic. It relies on the implementation object to do the actual low-level work.
- The `Implementation` declares the interface that’s common for all concrete implementations. An abstraction can only communicate with an implementation object via methods that are declared here.
- The abstraction may list the same methods as the implementation, but usually the abstraction declares some complex behaviors that rely on a wide variety of primitive operations declared by the implementation.
- Concrete Implementations contain platform-specific code.
- Refined Abstractions provide variants of control logic. Like their parent, they work with different implementations via the general implementation interface.
- Usually, the Client is only interested in working with the abstraction. However, it’s the client’s job to link the abstraction object with one of the implementation objects.

## Pseudocode
This example illustrates how the `Bridge` pattern can help divide the monolithic code of an app that manages devices and their remote controls. The **Device** classes act as the `implementation`, whereas the **Remotes** act as the `abstraction`.

<p style="text-align:center">
    <img src="../../static/bridge_psudocode.png"/>
</p>

The base remote control class declares a reference field that links it with a device object. All remotes work with the devices via the general device interface, which lets the same remote support multiple device types.
The client code links the desired type of remote control with a specific device object via the remote’s constructor.

```java
// The "abstraction" defines the interface for the "control"
// part of the two class hierarchies. It maintains a reference
// to an object of the "implementation" hierarchy and delegates
// all of the real work to this object.
class RemoteControl is
    protected field device: Device
    constructor RemoteControl(device: Device) is
        this.device = device
    method togglePower() is
        if (device.isEnabled()) then
            device.disable()
        else
            device.enable()
    method volumeDown() is
        device.setVolume(device.getVolume() - 10)
    method volumeUp() is
        device.setVolume(device.getVolume() + 10)
    method channelDown() is
        device.setChannel(device.getChannel() - 1)
    method channelUp() is
        device.setChannel(device.getChannel() + 1)


// You can extend classes from the abstraction hierarchy
// independently from device classes.
class AdvancedRemoteControl extends RemoteControl is
    method mute() is
        device.setVolume(0)


// The "implementation" interface declares methods common to all
// concrete implementation classes. It doesn't have to match the
// abstraction's interface. In fact, the two interfaces can be
// entirely different. Typically the implementation interface
// provides only primitive operations, while the abstraction
// defines higher-level operations based on those primitives.
interface Device is
    method isEnabled()
    method enable()
    method disable()
    method getVolume()
    method setVolume(percent)
    method getChannel()
    method setChannel(channel)


// All devices follow the same interface.
class Tv implements Device is
    // ...

class Radio implements Device is
    // ...


// Somewhere in client code.
tv = new Tv()
remote = new RemoteControl(tv)
remote.togglePower()

radio = new Radio()
remote = new AdvancedRemoteControl(radio)
```

## Applicability
- Use the Bridge pattern when you want to divide and organize a monolithic class that has several variants of some functionality (for example, if the class can work with various database servers).
- Use the pattern when you need to extend a class in several orthogonal (independent) dimensions.
- Use the Bridge if you need to be able to switch implementations at runtime.

##  How to Implement
- Identify the orthogonal dimensions in your classes. These independent concepts could be: abstraction/platform, domain/infrastructure, front-end/back-end, or interface/implementation.
- See what operations the client needs and define them in the base abstraction class.
- Determine the operations available on all platforms. Declare the ones that the abstraction needs in the general implementation interface.
- For all platforms in your domain create concrete implementation classes, but make sure they all follow the implementation interface.
- Inside the abstraction class, add a reference field for the implementation type. The abstraction delegates most of the work to the implementation object that’s referenced in that field.
- If you have several variants of high-level logic, create refined abstractions for each variant by extending the base abstraction class.
- The client code should pass an implementation object to the abstraction’s constructor to associate one with the other. After that, the client can forget about the implementation and work only with the abstraction object.

## Pros and Cons
## Pros
- You can create platform-independent classes and apps.
- The client code works with high-level abstractions. It isn’t exposed to the platform details.
- Open/Closed Principle. You can introduce new abstractions and implementations independently from each other.
- Single Responsibility Principle. You can focus on high-level logic in the abstraction and on platform details in the implementation.
## Cons
- You might make the code more complicated by applying the pattern to a highly cohesive class.

## Python Code Example

```python
# abstract_implementation.py
from abc import ABC, abstractmethod


class Implementation(ABC):
    """
    The Implementation defines the interface for all implementation 
	classes. It doesn't have to match the Abstraction's interface. 
	In fact, the two interfaces can be entirely different. Typically 
	the Implementation interface provides only primitive operations, 
	while the Abstraction defines higher-level operations based on those primitives.
    """

    @abstractmethod
    def operation_implementation(self) -> str:
        pass

# concrete_implementation.py
from abstract_implementation import Implementation

"""
Each Concrete Implementation corresponds to a specific platform 
and implements the Implementation interface using that platform's API.
"""

class ConcreteImplementationA(Implementation):
	def operation_implementation(self) -> str:
		return "ConcreteImplementationA: Here's the result on the platform A."

class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."

# abstraction.py
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

# extended_abstraction.py
from abstraction import Abstraction


class ExtendedAbstraction(Abstraction):
	"""
	You can extend the Abstraction without changing the Implementation classes.
	"""
	def operation(self) -> str:
		return (f"ExtendedAbstraction: Extended operation with:\n"
			f"{self.implementation.operation_implementation()}")

# main.py
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
```
```bash
Abstraction: Base operation with:
ConcreteImplementationA: Here's the result on the platform A.

ExtendedAbstraction: Extended operation with:
ConcreteImplementationB: Here's the result on the platform B.
```
