# Factory Pattern

**Classification**: Creational  
This pattern define an interface for subclass to create an object. But it lets subclass decide which object to create. It is also know as virtual constructor pattern.

##  Problem
Imagine that you’re creating a logistics management application. The first version of your app can only handle transportation by trucks, so the bulk of your code lives inside the `Truck` class.

At present, most of your code is coupled to the `Truck` class. Adding `Ships` into the app would require making changes to the entire codebase. Moreover, if later you decide to add another type of transportation to the app, you will probably need to make all of these changes again.

## Solution
The Factory Method pattern suggests that you replace direct object construction calls with calls to a special factory method. Objects returned by a factory method are often referred to as **products**. 

For example, both `Truck` and `Ship` classes should implement the `Transport` interface, which declares a method called `deliver`. Each class implements this method differently: `trucks` deliver cargo by land, `ships` deliver cargo by sea. 

The code that uses the factory method (often called the client code) doesn’t see a difference between the actual products returned by various subclasses. The client treats all the products as abstract `Transport`. The client knows that all transport objects are supposed to have the `deliver` method, but exactly how it works isn’t important to the client.

## Pseudocode
This example illustrates how the Factory Method can be used for creating cross-platform UI elements without coupling the client code to concrete UI classes.

<p style="text-align:center">
    <img src="../../static/factory_pattern.png"/>
</p>

For this pattern to work, the base dialog class must work with abstract buttons: a base class or an interface that all concrete buttons follow. This way the dialog’s code remains functional, whichever type of buttons it works with.

Of course, you can apply this approach to other UI elements as well. However, with each new factory method you add to the dialog, you get closer to the Abstract Factory pattern. 

## Applicability
- Use the Factory Method when you don’t know beforehand the exact types and dependencies of the objects your code should work with.
    - The Factory Method separates product construction code from the code that actually uses the product. Therefore it’s easier to extend the product construction code independently from the rest of the code.
- Use the Factory Method when you want to provide users of your library or framework with a way to extend its internal components.
    - Inheritance is probably the easiest way to extend the default behavior of a library or framework. But how would the framework recognize that your subclass should be used instead of a standard component? The solution is to reduce the code that constructs components across the framework into a single factory method and let anyone override this method in addition to extending the component itself.
- Use the Factory Method when you want to save system resources by reusing existing objects instead of rebuilding them each time.
    - You often experience this need when dealing with large, resource-intensive objects such as database connections, file systems, and network resources.
    - When someone requests an object, the program should look for a free object inside that pool and then return it to the client code. If there are no free objects, the program should create a new one (and add it to the pool).
    - Probably the most obvious and convenient place where this code could be placed is the constructor of the class whose objects we’re trying to reuse. However, a constructor must always return **new objects** by definition. It can’t return existing instances.

## How to Implement
1. Make all products follow the same interface. This interface should declare methods that make sense in every product.

2. Add an empty factory method inside the creator class. The return type of the method should match the common product interface.

3. In the creator’s code find all references to product constructors. One by one, replace them with calls to the factory method, while extracting the product creation code into the factory method.

4. You might need to add a temporary parameter to the factory method to control the type of returned product.

5. At this point, the code of the factory method may look pretty ugly. It may have a large `switch` operator that picks which product class to instantiate. But don’t worry, we’ll fix it soon enough.

6. Now, create a set of creator subclasses for each type of product listed in the factory method. Override the factory method in the subclasses and extract the appropriate bits of construction code from the base method.

7. If there are too many product types and it doesn’t make sense to create subclasses for all of them, you can reuse the control parameter from the base class in subclasses.

8. For instance, imagine that you have the following hierarchy of classes: the base `Mail` class with a couple of subclasses: `AirMail` and `GroundMail`; the `Transport` classes are `Plane`, `Truck` and `Train`. While the `AirMail` class only uses `Plane` objects, `GroundMail` may work with both `Truck` and `Train` objects. The client code can pass an argument to the factory method of the `GroundMail` class to control which product it wants to receive.

9. If, after all of the extractions, the base factory method has become empty, you can make it abstract. If there’s something left, you can make it a default behavior of the method.

## Pros and Cons

### Pros
1. You avoid tight coupling between the creator and the concrete products.
2. Single Responsibility Principle. You can move the product creation code into one place in the program, making the code easier to support.
3. Open/Closed Principle. You can introduce new types of products into the program without breaking existing client code.

### Cons
1. The code may become more complicated since you need to introduce a lot of new subclasses to implement the pattern. The best case scenario is when you’re introducing the pattern into an existing hierarchy of creator classes.

## Implementation

```python
# abstract_creator.py

from abc import ABC, abstractmethod


class Creator(ABC):
	"""
	The Creator class declares the factory method that is supposed to return an
	object of a Product class. The Creator's subclasses usually provide the
	implementation of this method.
	"""
	
	@abstractmethod
	def factory_method(self):
		"""
		Note that the Creator may also provide some default implementation of
		the factory method.
		"""
		pass

	def some_operation(self) -> str:
		"""
		Also note that, despite its name, the Creator's primary responsibility
		is not creating products. Usually, it contains some core business logic
		that relies on Product objects, returned by the factory method.
		Subclasses can indirectly change that business logic by overriding the
		factory method and returning a different type of product from it.
		"""

		# Call the factory method to create a Product object.
		product = self.factory_method()

		# Now, use the product.
		result = f"Creator: The same creator's code has just worked with {product.operation()}"

		return result
```

```python
# abstract_product.py

from abc import ABC, abstractmethod

class Product(ABC):
	"""
    The Product interface declares the operations that all concrete products
    must implement.
    """
	
	@abstractmethod
	def operations(self):
		pass
```

```python
# concrete_product.py

"""
Concrete Products provide various implementations of the Product interface.
"""
from abstract_product import Product


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"

```

```python
# concrete_creator.py

"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""

from abstract_creator import Creator
from abstract_product import Product
from concrete_product import ConcreteProduct1, ConcreteProduct2


class ConcreteCreator1(Creator):
	"""
	Note that the signature of the method still uses the abstract product type,
	even though the concrete product is actually returned from the method. This
	way the Creator can stay independent of concrete product classes.
	"""

	def factory_method(self) -> Product:
		return ConcreteProduct1()


class ConcreteCreator2(Creator):
	def factory_method(self) -> Product:
		return ConcreteProduct2()
```

```python
# main.py

from abstract_creator import Creator
from concrete_creator import ConcreteCreator1, ConcreteCreator2


def client_code(creator: Creator) -> None:
	"""
	The client code works with an instance of a concrete creator, albeit through
	its base interface. As long as the client keeps working with the creator via
	the base interface, you can pass it any creator's subclass.
	"""

	print(f"Client: I'm not aware of the creator's class, but it still works.\n"
		  f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
```

Here although `__main__` provide instance of `ConcreteCreator1` and `ConcreteCreator2` to the client code but that input can be anything like a string or number or boolean, basically for decision making. Also notice the code of client is intact and need not be changed in order to use different product. Also client just know the methods available on abstract creator so that it will remain intact with different creators.
