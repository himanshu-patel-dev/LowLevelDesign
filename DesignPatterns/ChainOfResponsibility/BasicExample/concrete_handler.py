from typing import Any
from abstract_handler import AbstractHandler

"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""

class MonkeyHandler(AbstractHandler):
	def handle(self, request: Any) -> str:
		if request == "Banana":
			return f"Monkey: I'll eat the {request}"
		else:
			return super().handle(request)

class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)
