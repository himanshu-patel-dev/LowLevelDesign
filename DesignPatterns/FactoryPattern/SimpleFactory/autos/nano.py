from .abstract_auto import AbstractAuto


class Nano(AbstractAuto):
    def start(self):
        print("Nano started")

    def stop(self):
        print("Nano stopped")
