# Abstract Factory Pattern

Abstract Factory is a creational design pattern, which solves the problem of creating entire product families without specifying their concrete classes.

## Problem

Imagine that you’re creating a furniture shop simulator. Your code consists of classes that represent:

1. A family of related products, say: `Chair` + `Sofa` + `CoffeeTable`.

2. Several variants of this family. For example, products `Chair` + `Sofa` + `CoffeeTable` are available in these variants: `Modern`, `Victorian`, `ArtDeco`.

<p style="text-align:center">
	<img src="../../static/furniture_types.png"/>
</p>

3. You need a way to create individual furniture objects so that they match other objects of the same family. Also, you don’t want to change existing code when adding new products or families of products to the program.

## Solution

The first thing the Abstract Factory pattern suggests is to explicitly declare interfaces for each distinct product of the product family (e.g., `chair`, `sofa` or `coffee` table). Then you can make all variants of products follow those interfaces. For example, all `chair` variants can implement the `Chair` interface; all `coffee` table variants can implement the `CoffeeTable` interface, and so on.

<p style="text-align:center">
	<img src="../../static/chair_interface.png"/>
</p>


The next move is to declare the `Abstract Factory`—an interface with a list of creation methods for all products that are part of the product family (for example, `createChair`, `createSofa` and `createCoffeeTable`). These methods must return abstract product types represented by the interfaces we extracted previously: `Chair`, `Sofa`, `CoffeeTable` and so on.

<p style="text-align:center">
	<img src="../../static/factory_interface.png"/>
</p>

The client code has to work with both factories and products via their respective abstract interfaces. This lets you change the type of a factory that you pass to the client code, as well as the product variant that the client code receives, without breaking the actual client code.

Product Type = `chair`, `sofa` or `coffee` table
Product Varient = `ModernChair`, `VictorianChair`, `ArtDecoChair`.

## Structure

1. **Abstract Products** declare interfaces for a set of distinct but related products which make up a product family.
2. **Concrete Products** are various implementations of abstract products, grouped by variants. Each abstract product (chair/sofa) must be implemented in all given variants (Victorian/Modern).
3. **The Abstract Factory** interface declares a set of methods for creating each of the abstract products.
4. **Concrete Factories** implement creation methods of the abstract factory. Each concrete factory corresponds to a specific variant of products and creates only those product variants.
5. Although concrete factories instantiate concrete products, signatures of their creation methods must return corresponding abstract products. This way the client code that uses a factory doesn’t get coupled to the specific variant of the product it gets from a factory. The **Client** can work with any concrete factory/product variant, as long as it communicates with their objects via abstract interfaces.

<p style="text-align:center">
	<img src="../../static/factory_abstract_structure.png"/>
</p>

## Applicability
- Use the Abstract Factory when your code needs to work with various families of related products, but you don’t want it to depend on the concrete classes of those products—they might be unknown beforehand or you simply want to allow for future extensibility.
- The Abstract Factory provides you with an interface for creating objects from each class of the product family. As long as your code creates objects via this interface, you don’t have to worry about creating the wrong variant of a product which doesn’t match the products already created by your app.
- Consider implementing the Abstract Factory when you have a class with a set of Factory Methods that blur its primary responsibility.
- In a well-designed program each class is responsible only for one thing. When a class deals with multiple product types, it may be worth extracting its factory methods into a stand-alone factory class or a full-blown Abstract Factory implementation.

## How to Implement
- Map out a matrix of distinct product types versus variants of these products.
- Declare abstract product interfaces for all product types. Then make all concrete product classes implement these interfaces.
- Declare the abstract factory interface with a set of creation methods for all abstract products.
- Implement a set of concrete factory classes, one for each product variant.
- Create factory initialization code somewhere in the app. It should instantiate one of the concrete factory classes, depending on the application configuration or the current environment. Pass this factory object to all classes that construct products.
- Scan through the code and find all direct calls to product constructors. Replace them with calls to the appropriate creation method on the factory object.

## Pros and Cons

### Pros
- You can be sure that the products you’re getting from a factory are compatible with each other.
- You avoid tight coupling between concrete products and client code.
- Single Responsibility Principle. You can extract the product creation code into one place, making the code easier to support.
- Open/Closed Principle. You can introduce new variants of products without breaking existing client code.
### Cons
- The code may become more complicated than it should be, since a lot of new interfaces and classes are introduced along with the pattern.

## Implementation

```python
from abc import ABC, abstractmethod
from abstract_products import AbstractProductA, AbstractProductB


class AbstractFactory(ABC):
	"""
	The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.
	"""

	@abstractmethod
	def create_product_a(self) -> AbstractProductA:
		pass

	@abstractmethod
	def create_product_b(self) -> AbstractProductB:
		pass	
```

```python
from abc import ABC, abstractmethod


class AbstractProductA(ABC):
	"""
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """
	@abstractmethod
	def useful_function_a(self) -> str:
		pass


class AbstractProductB(ABC):
    """
    Here's the the base interface of another product. All products can interact
    with each other, but proper interaction is possible only between products of
    the same concrete variant.
    """
    @abstractmethod
    def useful_function_b(self) -> None:
        """
        Product B is able to do its own thing...
        """
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        """
        ...but it also can collaborate with the ProductA.

        The Abstract Factory makes sure that all products it creates are of the
        same variant and thus, compatible.
        """
        pass
```

```python
from abstract_products import AbstractProductA, AbstractProductB
from abstract_factory import AbstractFactory
from concrete_products import ConcreteProductA1, ConcreteProductA2, ConcreteProductB1, ConcreteProductB2


class ConcreteFactory1(AbstractFactory):
	"""
	Concrete Factories produce a family of products that belong to a single
	variant. The factory guarantees that resulting products are compatible. Note
	that signatures of the Concrete Factory's methods return an abstract
	product, while inside the method a concrete product is instantiated.
	"""

	def create_product_a(self) -> AbstractProductA:
		return ConcreteProductA1()

	def create_product_b(self) -> AbstractProductB:
		return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
	"""
    Each Concrete Factory has a corresponding product variant.
    """
	def create_product_a(self) -> AbstractProductA:
		return ConcreteProductA2()

	def create_product_b(self) -> AbstractProductB:
		return ConcreteProductB2()
```

```python
from abstract_products import AbstractProductA, AbstractProductB


class ConcreteProductA1(AbstractProductA):
	def useful_function_a(self) -> str:
		return "The result of the product A1"


class ConcreteProductA2(AbstractProductA):
	def useful_function_a(self) -> str:
		return "The result of the product A2"


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    """
    The variant, Product B1, is only able to work correctly with the variant,
    Product A1. Nevertheless, it accepts any instance of AbstractProductA as an
    argument.
    """

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        """
        The variant, Product B2, is only able to work correctly with the
        variant, Product A2. Nevertheless, it accepts any instance of
        AbstractProductA as an argument.
        """
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"
```

```python
from abstract_factory import AbstractFactory
from concrete_facotries import ConcreteFactory1, ConcreteFactory2


def client_code(factory: AbstractFactory) -> None:
	"""
	The client code works with factories and products only through abstract
	types: AbstractFactory and AbstractProduct. This lets you pass any factory
	or product subclass to the client code without breaking it.
	"""
	product_a = factory.create_product_a()
	product_b = factory.create_product_b()
	
	print(f"{product_b.useful_function_b()}")
	print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
	"""
	The client code can work with any concrete factory class.
	"""
	
	print("Client: Testing client code with the first factory type:")
	client_code(ConcreteFactory1())

	print("\n")

	print("Client: Testing the same client code with the second factory type:")
	client_code(ConcreteFactory2())
```
