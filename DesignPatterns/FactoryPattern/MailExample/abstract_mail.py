from abc import ABC, abstractmethod


class Mail(ABC):
	@abstractmethod
	def get_transport(self):	# factory method - which each creator will implement
		"""
		Get the medium of transport
		"""

	def mail(self):
		"""
		mail the content using appropriate transport medium
		"""
		medium = self.get_transport()
		medium.deliver()
