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
