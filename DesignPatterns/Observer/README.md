# Observer Pattern

Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.


## Problem
A object wants to know about when a particular state of another object is achieved. Now there are two ways.
1. The object which need to know can constantly poll the target object, but this induce a lot or unnecessary polling.
2. The target object can broadcast it's state to all of the object waiting to know it's startus, but this will not be usefull for objects which do not want to be notified about all of the states of target but only some particular state.

## Solution
The object that has some interesting state is often called **subject**, but since it’s also going to notify other objects about the changes to its state, we’ll call it **publisher**. All other objects that want to track changes to the publisher’s state are called **subscribers**.

The Observer pattern suggests that you add a subscription mechanism to the publisher class so individual objects can subscribe to or unsubscribe from a stream of events coming from that publisher. All subscribers should implement the same interface and that the publisher communicates with them only via that interface. 

If your app has several different types of publishers and you want to make your subscribers compatible with all of them, you can go even further and make all publishers follow the same interface. This interface would only need to describe a few subscription methods. The interface would allow subscribers to observe publishers’ states without coupling to their concrete classes.

## Applicability
-  Use the Observer pattern when changes to the state of one object may require changing other objects, and the actual set of objects is unknown beforehand or changes dynamically.
- Use the pattern when some objects in your app must observe others, but only for a limited time or in specific cases.

## Pros
- Open/Closed Principle. You can introduce new subscriber classes without having to change the publisher’s code (and vice versa if there’s a publisher interface).
- You can establish relations between objects at runtime.
## Cons
- Subscribers are notified in random order.

## Implementation

```python
# subject.py
from abc import ABC, abstractmethod
from observer import Observer
from typing import List
from random import randrange


class Subject(ABC):
	"""
	The Subject interface declares a set of methods for managing subscribers.
	"""

	@abstractmethod
	def attach(self, observer: Observer) -> None:
		"""
		Attach an observer to the subject.
		"""
		pass
	
	@abstractmethod
	def detach(self, observer: Observer) -> None:
		"""
		Detach an observer from the subject.
		"""
		pass

	@abstractmethod
	def notify(self) -> None:
		"""
		Notify all observers about an event.
		"""
		pass


class ConcreteSubject(Subject):
	"""
	The Subject owns some important state and notifies observers when the state
	changes.
	"""
	_state: int = None

	"""
	For the sake of simplicity, the Subject's state, essential to all
	subscribers, is stored in this variable.
	"""
	_observers: List[Observer] = []
	
	"""
	List of subscribers. In real life, the list of subscribers can be stored
	more comprehensively (categorized by event type, etc.).
	"""

	def attach(self, observer: Observer) -> None:
		print("Subject: Attached an observer.")
		self._observers.append(observer)

	def detach(self, observer: Observer) -> None:
		self._observers.remove(observer)

	"""
	The subscription management methods.
	"""

	def notify(self) -> None:
		"""
		Trigger an update in each subscriber.
		"""

		print("Subject: Notifying observers...")
		for observer in self._observers:
			observer.update(self)
	
	def some_business_logic(self) -> None:
		"""
		Usually, the subscription logic is only a fraction of what a Subject can
		really do. Subjects commonly hold some important business logic, that
		triggers a notification method whenever something important is about to
		happen (or after it).
		"""

		print("\nSubject: I'm doing something important.")
		self._state = randrange(0, 10)

		print(f"Subject: My state has just changed to: {self._state}")
		self.notify()


# observer.py
from abc import ABC, abstractmethod


class Observer(ABC):
	"""
	The Observer interface declares the update method, used by subjects.
	"""

	@abstractmethod
	def update(self, subject) -> None:
		"""
		Receive update from subject.
		"""
		pass

"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""

class ConcreteObserverA(Observer):
    def update(self, subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")

# main.py
from observer import ConcreteObserverA, ConcreteObserverB
from subject import ConcreteSubject


if __name__ == "__main__":
	subject = ConcreteSubject()
	
	observer_a = ConcreteObserverA()
	observer_b = ConcreteObserverB()

	subject.attach(observer_a)
	subject.attach(observer_b)

	subject.some_business_logic()
	subject.some_business_logic()

	subject.detach(observer_a)

	subject.some_business_logic()
```
```bash
Subject: Attached an observer.
Subject: Attached an observer.

Subject: I'm doing something important.
Subject: My state has just changed to: 8
Subject: Notifying observers...
ConcreteObserverB: Reacted to the event

Subject: I'm doing something important.
Subject: My state has just changed to: 1
Subject: Notifying observers...
ConcreteObserverA: Reacted to the event

Subject: I'm doing something important.
Subject: My state has just changed to: 2
Subject: Notifying observers...
ConcreteObserverB: Reacted to the event
```
