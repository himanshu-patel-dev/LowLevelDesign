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
