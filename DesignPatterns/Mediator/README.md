# Mediator Pattern

Mediator is a behavioral design pattern that reduces coupling between components of a program by making them communicate indirectly, through a special mediator object

# Applicability
- Use the Mediator pattern when it’s hard to change some of the classes because they are tightly coupled to a bunch of other classes. Because the pattern lets you extract all the relationships between classes into a separate class, isolating any changes to a specific component from the rest of the components.
- Use the pattern when you can’t reuse a component in a different program because it’s too dependent on other components.
- Use the Mediator when you find yourself creating tons of component subclasses just to reuse some basic behavior in various contexts.

## Pros
- Single Responsibility Principle. You can extract the communications between various components into a single place, making it easier to comprehend and maintain.
- Open/Closed Principle. You can introduce new mediators without having to change the actual components.
- You can reduce coupling between various components of a program.
- You can reuse individual components more easily.
## Cons
- Over time a mediator can evolve into a God Object.

```python
# component.py
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

# mediator.py
from abc import ABC, abstractmethod


class Mediator(ABC):
	"""
	The Mediator interface declares a method used by components to notify the
	mediator about various events. The Mediator may react to these events and
	pass the execution to other components.
	"""
	@abstractmethod
	def notify(self, sender: object, event: str) -> None:
		pass


class ConcreteMediator(Mediator):
	def __init__(self, component1, component2) -> None:
		self._component1 = component1
		self._component1.mediator = self
		self._component2 = component2
		self._component2.mediator = self
	
	def notify(self, sender: object, event: str) -> None:
		if event == "A":
			print("Mediator reacts on A and triggers following operations:")
			self._component2.do_c()
		elif event == "D":
			self._component1.do_b()
			self._component2.do_c()

# main.py
from component import Component1, Component2
from mediator import ConcreteMediator


if __name__ == "__main__":
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)

    print("Client triggers operation A.")
    c1.do_a()

    print("\n", end="")

    print("Client triggers operation D.")
    c2.do_d()
```
```bash
Client triggers operation A.
Component 1 does A.
Mediator reacts on A and triggers following operations:
Component 2 does C.

Client triggers operation D.
Component 2 does D.
Component 1 does B.
Component 2 does C.
```

**Be careful while programming a mediator like this and don't end up creating an infinite loop of event recursion. Note here the mediator do not react on event B and C and hence prevent forming and event loop.**
