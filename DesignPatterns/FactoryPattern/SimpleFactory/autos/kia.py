from .abstract_auto import AbstractAuto


class Kia(AbstractAuto):
    def start(self):
        print("Kia started")

    def stop(self):
        print("Kia stopped")
