from .abstract_factory import AbsFactory
from autos.nexon import Nexon


class NexonFactory(AbsFactory):

    def create_auto(self):
        self.nexon = nexon = Nexon()
        nexon.name = 'Nexon SUV'
        return nexon
