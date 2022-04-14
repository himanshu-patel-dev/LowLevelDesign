from operator import delitem
from abstract_transport import Transport


class Truck(Transport):
	def deliver(self):
		print("Deliver via Truck")


class Train(Transport):
	def deliver(self):
		print("Deliver via Train")


class Plane(Transport):
	def deliver(self):
		print("Deliver via Plane")
