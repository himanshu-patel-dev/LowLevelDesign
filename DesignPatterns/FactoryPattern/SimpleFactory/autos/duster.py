from .abstract_auto import AbstractAuto


class Duster(AbstractAuto):
    def start(self):
        print("Duster started")

    def stop(self):
        print("Duster stopped")
