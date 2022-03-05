from .abstract_auto import AbstractAuto


class Nexon(AbstractAuto):
    def start(self):
        print("Nexon started")

    def stop(self):
        print("Nexon stopped")
