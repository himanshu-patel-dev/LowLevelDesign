from .abstract_auto import AbstractAuto


class Kia(AbstractAuto):
    # def __init__(self, name):
    #     self.name = name

    def start(self):
        print(f"{self.name} started")

    def stop(self):
        print(f"{self.name} stopped")
