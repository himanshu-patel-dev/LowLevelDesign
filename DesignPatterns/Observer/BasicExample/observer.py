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
