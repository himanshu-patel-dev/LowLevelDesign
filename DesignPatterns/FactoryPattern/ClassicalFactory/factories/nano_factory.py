from .abstract_factory import AbsFactory
from autos.nano import Nano


class NanoFactory(AbsFactory):

    def create_auto(self):
        self.nano = nano = Nano()
        nano.name = 'Nano Car'
        return nano
