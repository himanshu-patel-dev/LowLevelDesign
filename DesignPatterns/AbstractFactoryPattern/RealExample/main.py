from pydoc import cli
from abstract_factory import AbstractFactory
from concrete_factories import WoodenFactory, MetallicFactory


def client_code(factory: AbstractFactory):
	chair = factory.get_chair()
	sofa = factory.get_sofa()

	print(f"Chair: {chair.sit_on()}")
	print(f"Sofa: {sofa.sleep_on()}")


if __name__ == "__main__":
	client_code(WoodenFactory())
	client_code(MetallicFactory())
