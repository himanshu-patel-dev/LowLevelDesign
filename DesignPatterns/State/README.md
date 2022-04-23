# State Pattern
State is a behavioral design pattern that lets an object alter its behavior when its internal state changes. It appears as if the object changed its class.

## Problem
The State pattern is closely related to the concept of a **Finite-State Machine**.

The main idea is that, at any given moment, there’s a finite number of states which a program can be in. Within any unique state, the program behaves differently, and the program can be switched from one state to another instantaneously. However, depending on a current state, the program may or may not switch to certain other states. These switching rules, called transitions, are also finite and predetermined.

You can also apply this approach to objects. Imagine that we have a `Document` class. A document can be in one of three states: `Draft`, `Moderation` and `Published`. The `publish` method of the document works a little bit differently in each state:

- In `Draft`, it moves the document to oderation.
- In `Moderation`, it makes the document public, but only if the current user is an administrator.
- In `Published`, it doesn’t do anything at all.

The problem tends to get bigger as a project evolves. It’s quite difficult to predict all possible states and transitions at the design stage. Hence, a lean state machine built with a limited set of conditionals can grow into a bloated mess over time.

## Solution
The State pattern suggests that you create new classes for all possible states of an object and extract all state-specific behaviors into these classes.

Instead of implementing all behaviors on its own, the original object, called context, stores a reference to one of the state objects that represents its current state, and delegates all the state-related work to that object.

To transition the context into another state, replace the active state object with another object that represents that new state. This is possible only if all state classes follow the same interface and the context itself works with these objects through that interface.

This structure may look similar to the Strategy pattern, but there’s one key difference. In the State pattern, the particular states may be aware of each other and initiate transitions from one state to another, whereas strategies almost never know about each other.

## Applicability
- Use the State pattern when you have an object that behaves differently depending on its current state, the number of states is enormous, and the state-specific code changes frequently.
- Use the pattern when you have a class polluted with massive conditionals that alter how the class behaves according to the current values of the class’s fields.
- Use State when you have a lot of duplicate code across similar states and transitions of a condition-based state machine.

## Pros
- Single Responsibility Principle. Organize the code related to particular states into separate classes.
- Open/Closed Principle. Introduce new states without changing existing state classes or the context.
- Simplify the code of the context by eliminating bulky state machine conditionals.
## Cons
- Applying the pattern can be overkill if a state machine has only a few states or rarely changes.

## Implementation

```python
# state.py
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

# context.py
from abc import ABC, abstractmethod


class State(ABC):
	"""
	The base State class declares methods that all Concrete State should
	implement and also provides a backreference to the Context object,
	associated with the State. This backreference can be used by States to
	transition the Context to another State.
	"""
	@property
	def context(self):
		return self._context

	@context.setter
	def context(self, context):
		self._context = context

	@abstractmethod
	def handle1(self) -> None:
		pass

	@abstractmethod
	def handle2(self) -> None:
		pass

"""
Concrete States implement various behaviors, associated with a state of the Context.
"""

class ConcreteStateA(State):
	def handle1(self) -> None:
		print("ConcreteStateA handles request1.")
		print("ConcreteStateA wants to change the state of the context.")
		self.context.transition_to(ConcreteStateB())

	def handle2(self) -> None:
		print("ConcreteStateA handles request2.")


class ConcreteStateB(State):
	def handle1(self) -> None:
		print("ConcreteStateB handles request1.")

	def handle2(self) -> None:
		print("ConcreteStateB handles request2.")
		print("ConcreteStateB wants to change the state of the context.")
		self.context.transition_to(ConcreteStateA())

# main.py
from context import Context
from state import ConcreteStateA


if __name__ == "__main__":
	# The client code.

	context = Context(ConcreteStateA())
	context.request1()
	print('---')
	context.request2()
```
```bash
Context: Transition to ConcreteStateA
ConcreteStateA handles request1.
ConcreteStateA wants to change the state of the context.
Context: Transition to ConcreteStateB
---
ConcreteStateB handles request2.
ConcreteStateB wants to change the state of the context.
Context: Transition to ConcreteStateA
```
