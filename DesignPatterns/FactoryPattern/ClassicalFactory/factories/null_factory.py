from .abstract_factory import AbsFactory
from autos.null_car import NullCar


class NullFactory(AbsFactory):

    def create_auto(self):
        self.nullcar = nullcar = NullCar()
        nullcar.name = 'Unknown'
        return nullcar
