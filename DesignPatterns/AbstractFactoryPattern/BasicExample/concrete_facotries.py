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
