from .abstract_factory import AbsFactory
from autos.kia import Kia


class KiaFactory(AbsFactory):

    def create_auto(self):
        self.kia = kia = Kia()
        kia.name = 'Kia SUV'
        return kia
