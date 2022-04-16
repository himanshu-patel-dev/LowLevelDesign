# Builder Pattern

**Classification**: Creational  
This pattern is used for creation of object. The intent of the Builder design pattern is to separate the construction of a complex object from its representation. By doing so, the same construction process can create different representations.  

## Problem
Imagine a complex object that requires laborious, step-by-step initialization of many fields and nested objects. Such initialization code is usually buried inside a monstrous constructor with lots of parameters. Or even worse: scattered all over the client code.

## Solution
The Builder pattern suggests that you extract the object construction code out of its own class and move it to separate objects called `builders`.

#### Director
You can go further and extract a series of calls to the builder steps you use to construct a product into a separate class called `director`. The director class defines the order in which to execute the building steps, while the builder provides the implementation for those steps.

Having a director class in your program isn’t strictly necessary. You can always call the building steps in a specific order directly from the client code. However, the director class might be a good place to put various construction routines so you can reuse them across your program.

## Structure
1. The Builder `interface` declares product construction steps that are common to all types of builders.
2. Concrete Builders provide different implementations of the construction steps. Concrete builders may produce products that don’t follow the common interface.
3. Products are resulting objects. Products constructed by different builders don’t have to belong to the same class hierarchy or interface.
4. The Director class defines the order in which to call construction steps, so you can create and reuse specific configurations of products.
5. The `Client` must associate one of the builder objects with the director. Usually, it’s done just once, via parameters of the director’s constructor. Then the director uses that builder object for all further construction. However, there’s an alternative approach for when the client passes the builder object to the production method of the director. In this case, you can use a different builder each time you produce something with the director.

## Applicability
- Use the Builder pattern to get rid of a “telescopic constructor”.
- Use the Builder pattern when you want your code to be able to create different representations of some product (for example, stone and wooden houses).
- Use the Builder to construct Composite trees or other complex objects.

## Pros and Cons

### Pros
- You can construct objects step-by-step, defer construction steps or run steps recursively.
- You can reuse the same construction code when building various representations of products.
- Single Responsibility Principle. You can isolate complex construction code from the business logic of the product.
#### Cons
- The overall complexity of the code increases since the pattern requires creating multiple new classes.

## Implementation

```python
# product.py
class Product1:
	"""
	It makes sense to use the Builder pattern only when your products are quite
	complex and require extensive configuration.

	Unlike in other creational patterns, different concrete builders can produce
	unrelated products. In other words, results of various builders may not
	always follow the same interface.
	"""

	def __init__(self) -> None:
		self.parts = []

	def add(self, part) -> None:
		self.parts.append(part)

	def list_parts(self) -> None:
		print(f"Product parts : {','.join(self.parts)}")
```

```python
# abstract_builder.py
from abc import ABC, abstractmethod, abstractproperty


class Builder(ABC):
	"""
	The Builder interface specifies methods for creating the different parts of
	the Product objects.
	"""

	@abstractproperty
	def product(self) -> None:
		pass

	@abstractmethod
	def produce_part_a(self) -> None:
		pass

	@abstractmethod
	def produce_part_b(self) -> None:
		pass

	@abstractmethod
	def produce_part_c(self) -> None:
		pass
```

```python
# concrete_builder.py
from abstract_builder import Builder
from product import Product1


class ConcreteBuilder1(Builder):	
	"""
	The Concrete Builder classes follow the Builder interface and provide
	specific implementations of the building steps. Your program may have
	several variations of Builders, implemented differently.
	"""
	def __init__(self) -> None:
		"""
		A fresh builder instance should contain a blank product object, which is
		used in further assembly.
		"""
		self.reset()

	def reset(self) -> None:
		self._product = Product1()

	@property
	def product(self) -> Product1:
		"""
		Concrete Builders are supposed to provide their own methods for
		retrieving results. That's because various types of builders may create
		entirely different products that don't follow the same interface.
		Therefore, such methods cannot be declared in the base Builder interface
		(at least in a statically typed programming language).

		Usually, after returning the end result to the client, a builder
		instance is expected to be ready to start producing another product.
		That's why it's a usual practice to call the reset method at the end of
		the `getProduct` method body. However, this behavior is not mandatory,
		and you can make your builders wait for an explicit reset call from the
		client code before disposing of the previous result.
		"""
		product = self._product
		self.reset()
		return product

	def produce_part_a(self) -> None:
		self._product.add("PartA1")

	def produce_part_b(self) -> None:
		self._product.add("PartB1")

	def produce_part_c(self) -> None:
		self._product.add("PartC1")
```

```python
# director.py
from abstract_builder import Builder


class Director:
	"""
	The Director is only responsible for executing the building steps in a
	particular sequence. It is helpful when producing products according to a
	specific order or configuration. Strictly speaking, the Director class is
	optional, since the client can control builders directly.
	"""
	
	def __init__(self) -> None:
		self._builder = None

	@property
	def builder(self) -> Builder:
		return self._builder

	@builder.setter
	def builder(self, builder: Builder) -> None:
		"""
		The Director works with any builder instance that the client code passes
		to it. This way, the client code may alter the final type of the newly
		assembled product.
		"""
		self._builder = builder
		

	"""
	The Director can construct several product variations using the same
	building steps.
	"""

	def build_minimal_viable_product(self) -> None:
		self.builder.produce_part_a()

	def build_full_featured_product(self) -> None:
		self.builder.produce_part_a()
		self.builder.produce_part_b()
		self.builder.produce_part_c()
```

```python
# main.py
from director import Director
from concrete_builder import ConcreteBuilder1


def client_code():
	"""
	The client code creates a builder object, passes it to the director and then
	initiates the construction process. The end result is retrieved from the
	builder object.
	"""

	director = Director()
	builder = ConcreteBuilder1()
	director.builder = builder
	
	print("Starndard basic product: ")
	director.build_minimal_viable_product()	# director use builder to make MVP
	builder.product.list_parts()

	print()

	print("Standard full featured product: ")
	director.build_full_featured_product()
	builder.product.list_parts()

	print()

	# Remember, the Builder pattern can be used without a Director class.
	print("Custom product: ")
	builder.produce_part_a()
	builder.produce_part_b()
	builder.product.list_parts()


if __name__ == "__main__":
	client_code()
```
