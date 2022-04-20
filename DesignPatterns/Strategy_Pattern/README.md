# Strategy Pattern

Strategy is a behavioral design pattern that turns a set of behaviors into objects and makes them interchangeable inside original context object.

The original object, called **context**, holds a reference to a **strategy object** and delegates it executing the behavior. In order to change the way the context performs its work, other objects may replace the currently linked strategy object with another one.

## Identification
Strategy pattern can be recognized by a method that lets nested object do the actual work, as well as the setter that allows replacing that object with a different one.

## Applicability
- Use the Strategy pattern when you want to use different variants of an algorithm within an object and be able to switch from one algorithm to another during runtime.
- Use the Strategy when you have a lot of similar classes that only differ in the way they execute some behavior.
- Use the pattern to isolate the business logic of a class from the implementation details of algorithms that may not be as important in the context of that logic.
- Use the pattern when your class has a massive conditional operator that switches between different variants of the same algorithm.

## How to Implement
- In the context class, identify an algorithm that’s prone to frequent changes. It may also be a massive conditional that selects and executes a variant of the same algorithm at runtime.
- Declare the strategy interface common to all variants of the algorithm.
- One by one, extract all algorithms into their own classes. They should all implement the strategy interface.
- In the context class, add a field for storing a reference to a strategy object. Provide a setter for replacing values of that field. The context should work with the strategy object only via the strategy interface. The context may define an interface which lets the strategy access its data.
- Clients of the context must associate it with a suitable strategy that matches the way they expect the context to perform its primary job.

## Pros
- You can swap algorithms used inside an object at runtime.
- You can isolate the implementation details of an algorithm from the code that uses it.
- You can replace inheritance with composition.
- Open/Closed Principle. You can introduce new strategies without having to change the context.

## Cons
- If you only have a couple of algorithms and they rarely change, there’s no real reason to overcomplicate the program with new classes and interfaces that come along with the pattern.
- Clients must be aware of the differences between strategies to be able to select a proper one.
- A lot of modern programming languages have functional type support that lets you implement different versions of an algorithm inside a set of anonymous functions. Then you could use these functions exactly as you’d have used the strategy objects, but without bloating your code with extra classes and interfaces.


```python
# strategy.py
from abc import ABC, abstractmethod
from typing import List


class Strategy(ABC):
	"""
	The Strategy interface declares operations common to all supported versions
	of some algorithm.

	The Context uses this interface to call the algorithm defined by Concrete
	Strategies.
	"""
	@abstractmethod
	def do_algorithm(self, data: List):
		pass

"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""

class ConcreteStrategyA(Strategy):
	def do_algorithm(self, data: List):
		return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorfrom strategy import Strategy


class Context:
	"""
	The Context defines the interface of interest to clients.
	"""

	def __init__(self, strategy: Strategy) -> None:
		"""
		Usually, the Context accepts a strategy through the constructor, but
		also provides a setter to change it at runtime.
		"""
		self._strategy = strategy

	@property
	def strategy(self) -> Strategy:
		"""
		The Context maintains a reference to one of the Strategy objects. The
		Context does not know the concrete class of a strategy. It should work
		with all strategies via the Strategy interface.
		"""
		return self._strategy

	@strategy.setter
	def strategy(self, strategy: Strategy) -> None:
		"""
		Usually, the Context allows replacing a Strategy object at runtime.
		"""
		self._strategy = strategy

	def do_some_business_logic(self) -> None:
		"""
		The Context delegates some work to the Strategy object instead of
		implementing multiple versions of the algorithm on its own.
		"""
		print("Context: Sorting data using the strategy")
		result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
		print(",".join(result))
ted(data))

# context.py
from strategy import Strategy


class Context:
	"""
	The Context defines the interface of interest to clients.
	"""

	def __init__(self, strategy: Strategy) -> None:
		"""
		Usually, the Context accepts a strategy through the constructor, but
		also provides a setter to change it at runtime.
		"""
		self._strategy = strategy

	@property
	def strategy(self) -> Strategy:
		"""
		The Context maintains a reference to one of the Strategy objects. The
		Context does not know the concrete class of a strategy. It should work
		with all strategies via the Strategy interface.
		"""
		return self._strategy

	@strategy.setter
	def strategy(self, strategy: Strategy) -> None:
		"""
		Usually, the Context allows replacing a Strategy object at runtime.
		"""
		self._strategy = strategy

	def do_some_business_logic(self) -> None:
		"""
		The Context delegates some work to the Strategy object instead of
		implementing multiple versions of the algorithm on its own.
		"""
		print("Context: Sorting data using the strategy")
		result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
		print(",".join(result))

# main.py
from context import Context
from strategy import ConcreteStrategyA, ConcreteStrategyB


if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.
		
    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()
```
```bash
Client: Strategy is set to normal sorting.
Context: Sorting data using the strategy
a,b,c,d,e

Client: Strategy is set to reverse sorting.
Context: Sorting data using the strategy
e,d,c,b,a
```
