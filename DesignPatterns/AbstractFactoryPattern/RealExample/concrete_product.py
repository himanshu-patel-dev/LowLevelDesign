from abstract_product import Chair, Sofa


class MetallicChair(Chair):
	def sit_on(self):
		return "Sit on Metallic Chair"

class MetallicSofa(Sofa):
	def sleep_on(self):
		return "Sleep on Metallic Sofa"

class WoodenChair(Chair):
	def sit_on(self):
		return "Sit on Wooden Chair"

class WoodenSofa(Sofa):
	def sleep_on(self):
		return "Sleep on Wooden Sofa"
