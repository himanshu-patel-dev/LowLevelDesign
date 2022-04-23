# Command Pattern

Command is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. This transformation lets you pass requests as a method arguments, delay or queue a request’s execution, and support undoable operations.

## Problem

Imagine that you’re working on a new text-editor app. Your current task is to create a toolbar with a bunch of buttons for various operations of the editor. You created a very neat `Button` class that can be used for buttons on the toolbar, as well as for generic buttons in various dialogs.

While all of these buttons look similar, they’re all supposed to do different things. Where would you put the code for the various click handlers of these buttons? The simplest solution is to create tons of subclasses for each place where the button is used. These subclasses would contain the code that would have to be executed on a button click.

## Solution

Good software design is often based on the **principle of separation of concerns**, which usually results in breaking an app into layers. 

In the code it might look like this: a GUI object calls a method of a business logic object, passing it some arguments. This process is usually described as one object sending another a request.

<p style="text-align:center">
    <img src="../../static/command_normal.png"/>
</p>

The Command pattern suggests that GUI objects shouldn’t send these requests directly. Instead, you should extract all of the request details, such as the object being called, the name of the method and the list of arguments into a separate `command` class with a single method that triggers this request.

<p style="text-align:center">
    <img src="../../static/command_expected.png"/>
</p>

## Applicability
- Use the Command pattern when you want to parametrize objects with operations.
- Use the Command pattern when you want to queue operations, schedule their execution, or execute them remotely.
- Use the Command pattern when you want to implement reversible operations.

## Pros
- Single Responsibility Principle. You can decouple classes that invoke operations from classes that perform these operations.
- Open/Closed Principle. You can introduce new commands into the app without breaking existing client code.
- You can implement undo/redo.
- You can implement deferred execution of operations.
- You can assemble a set of simple commands into a complex one.
## Cons
- The code may become more complicated since you’re introducing a whole new layer between senders and receivers.

## Implementation

```python
# receiver.py
class Receiver:
	"""
	The Receiver classes contain some important business logic. They know how to
	perform all kinds of operations, associated with carrying out a request. In
	fact, any class may serve as a Receiver.
	"""
	def do_something(self, a: str) -> None:
		print(f"\nReceiver: Working on ({a}.)", end="")

	def do_something_else(self, b: str) -> None:
		print(f"\nReceiver: Also working on ({b}.)", end="")

# command.py
from abc import ABC, abstractmethod
from receiver import Receiver


class Command(ABC):
	"""
	The Command interface declares a method for executing a command.
	"""

	@abstractmethod
	def execute(self) -> None:
		pass
	

class SimpleCommand(Command):
	"""
	Some commands can implement simple operations on their own.
	"""

	def __init__(self, payload: str) -> None:
		self._payload = payload

	def execute(self) -> None:
		print(f"SimpleCommand: See, I can do simple things like printing"
			  f"({self._payload})")


class ComplexCommand(Command):
	"""
	However, some commands can delegate more complex operations to other
	objects, called "receivers."
	"""

	def __init__(self, receiver: Receiver, a: str, b: str) -> None:
		"""
		Complex commands can accept one or several receiver objects along with
		any context data via the constructor.
		"""

		self._receiver = receiver
		self._a = a
		self._b = b
		
	def execute(self) -> None:
		"""
		Commands can delegate to any methods of a receiver.
		"""
		print("ComplexCommand: Complex stuff should be done by a receiver object", end="")
		self._receiver.do_something(self._a)
		self._receiver.do_something_else(self._b)


# invoker.py
from command import Command


class Invoker:
	"""
	The Invoker is associated with one or several commands. It sends a request
	to the command.
	"""
	_on_start = None
	_on_finish = None

	"""
	Initialize commands.
	"""

	def set_on_start(self, command: Command):
		self._on_start = command

	def set_on_finish(self, command: Command):
		self._on_finish = command
	
	def do_something_important(self) -> None:
		"""
		The Invoker does not depend on concrete command or receiver classes. The
		Invoker passes a request to a receiver indirectly, by executing a
		command.
		"""
		
		print("Invoker: Does anybody want something done before I begin?")
		if isinstance(self._on_start, Command):
			self._on_start.execute()

		print("Invoker: ...doing something really important...")

		print("Invoker: Does anybody want something done after I finish?")
		if isinstance(self._on_finish, Command):
			self._on_finish.execute()

# main.py
from invoker import Invoker
from command import SimpleCommand, ComplexCommand
from receiver import Receiver


if __name__ == "__main__":
    """
    The client code can parameterize an invoker with any commands.
    """

    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(
        receiver, "Send email", "Save report"))

    invoker.do_something_important()
```
```bash
Invoker: Does anybody want something done before I begin?
SimpleCommand: See, I can do simple things like printing(Say Hi!)
Invoker: ...doing something really important...
Invoker: Does anybody want something done after I finish?
ComplexCommand: Complex stuff should be done by a receiver object
Receiver: Working on (Send email.)
Receiver: Also working on (Save report.)
```
