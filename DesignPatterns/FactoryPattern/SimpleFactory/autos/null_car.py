from .abstract_auto import AbstractAuto


class NullCar(AbstractAuto):
    def __init__(self, carname):
        self._carname = carname

    def start(self):
        print('Unknown car "%s".' % self._carname)

    def stop(self):
        pass
