from abc import ABC, abstractmethod
from abstract_product import Chair, Sofa


class AbstractFactory(ABC):
	@abstractmethod
	def get_chair(self) -> Chair:
		pass

	def get_sofa(self) -> Sofa:
		pass
