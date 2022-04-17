class Component:
	"""
	The base Component interface defines operations that can be altered by
	decorators.
	"""
	def operations(self) -> str:
		pass


class ConcreteComponent(Component):
    """
    Concrete Components provide default implementations of the operations. There
    might be several variations of these classes.
    """

    def operation(self) -> str:
        return "ConcreteComponent"
