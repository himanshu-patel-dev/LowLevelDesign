from abc import ABC, abstractmethod, abstractproperty

class Switchable(ABC):
	@abstractmethod
	def turn_on(self):
		pass
	
	@abstractmethod
	def turn_off(self):
		pass

	@abstractproperty
	def device(self):
		pass

# we can't instantiate an abstract class neither any other 
# class which inherit abstract class and do not implement 
# even one of its abstractmethod or abstractproperty

# s = Switchable()


class LightBulb(Switchable):
	def turn_on(self):
		print('LightBulb: turned on')

	def turn_off(self):
		print('LightBulb: turned off')

	@property
	def device(self):
		return "Bulb"

class Fan(Switchable):
	def turn_on(self):
		print('Fan: turn on')

	def turn_off(self):
		print('Fan: turn off')

	@property
	def device(self):
		return "Fan"


class ElectricPowerSwitch:
	def __init__(self, c: Switchable):
		self.client = c
		self.on = False

	def press(self):
		if self.on:
			self.client.turn_off()
			self.on = False
		else:
			self.client.turn_on()
			self.on = True

b = LightBulb()
f = Fan()
switch = ElectricPowerSwitch(b)
switch.press()
switch.press()
print(switch.client.device)
