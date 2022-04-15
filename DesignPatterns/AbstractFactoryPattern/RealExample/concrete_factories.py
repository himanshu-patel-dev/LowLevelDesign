from abstract_factory import AbstractFactory
from concrete_product import MetallicChair, MetallicSofa, WoodenChair, WoodenSofa


class WoodenFactory(AbstractFactory):
	def get_chair(self):
		return WoodenChair()

	def get_sofa(self):
		return WoodenSofa()

class MetallicFactory(AbstractFactory):
	def get_chair(self):
		return MetallicChair()

	def get_sofa(self):
		return MetallicSofa()
