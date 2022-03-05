from .abstract_auto import AbstractAuto


class Nexon(AbstractAuto):
    def start(self):
        print(f"{self.name} started")

    def stop(self):
        print(f"{self.name} stopped")
