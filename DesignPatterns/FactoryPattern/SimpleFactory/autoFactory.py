from inspect import isclass, isabstract, getmembers
import autos


def isconcrete(obj):
    return isclass(obj) and not isabstract(obj)


class AutoFactory:
    vehicles = {}      # { car model name: class for the car}

    def __init__(self):
        self.load_autos()

    def load_autos(self):
        classes = getmembers(autos, isconcrete)

        for name, _type in classes:
            if isclass(_type) and issubclass(_type, autos.AbstractAuto):
                self.vehicles.update([[name, _type]])

    def create_instance(self, carname):
        if carname in self.vehicles:
            return self.vehicles[carname]()
        return autos.NullCar(carname)
