from abstract_mail import Mail
from product_transport import Train, Truck, Plane


class AirMail(Mail):
	def get_transport(self):
		return Plane()

class RailMail(Mail):
	def get_transport(self):
		return Train()

class LandMail(Mail):
	def get_transport(self):
		return Truck()