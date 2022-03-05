# Factory Pattern

**Classification**: Creational  
This pattern define an interface for subclass to create an object. But it lets subclass decide which object to create. It is also know as virtual constructor pattern.

First we make a `Abstract Base Class` and then make concrete classes based on this only.

```python
# abstract_auto.py
from abc import ABC, abstractmethod


class AbstractAuto(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
```

```python
# implement all concrete class whome we want to instantiate

from .abstract_auto import AbstractAuto


class Duster(AbstractAuto):
    def start(self):
        print("Duster started")

    def stop(self):
        print("Duster stopped")

class Kia(AbstractAuto):
    def start(self):
        print("Kia started")

    def stop(self):
        print("Kia stopped")


class Nano(AbstractAuto):
    def start(self):
        print("Nano started")

    def stop(self):
        print("Nano stopped")

class Nexon(AbstractAuto):
    def start(self):
        print("Nexon started")

    def stop(self):
        print("Nexon stopped")


class NullCar(AbstractAuto):
    def __init__(self, carname):
        self._carname = carname

    def start(self):
        print('Unknown car "%s".' % self._carname)

    def stop(self):
        pass
```

To access all the class we declared here in `autos` package we need to bring all those classes to `__init__.py` file as this is the only file which gets loaded into module which calls `import autos`. Also notice the way we called adjacent files using a period `.` before the name of file. This is not done when we import the neighbout module as library for instantiation.

```python
from .duster import Duster
from .nano import Nano
from .kia import Kia
from .nexon import Nexon
from .abstract_auto import AbstractAuto
```

## Simple Factory

Now is the time when we make a factory which takes a class name as string and return its object. To do this we basically make a mapping for each classname and its class. When called with a name as string we return corresponding classes object.

```python
from inspect import isclass, isabstract, getmembers
import autos


def isconcrete(obj):
    return isclass(obj) and not isabstract(obj)


class AutoFactory:
    vehicles = {}      # { car model name: class for the car}

    def __init__(self):
        self.load_autos()

    def load_autos(self):
        classes = getmembers(autos, isconcrete)

        for name, _type in classes:
            if isclass(_type) and issubclass(_type, autos.AbstractAuto):
                self.vehicles.update([[name, _type]])

    def create_instance(self, carname):
        if carname in self.vehicles:
            return self.vehicles[carname]()
        return autos.NullCar(carname)
```

Python main file for execution.

```python
from autoFactory import AutoFactory

factory = AutoFactory()

for carname in ['Nano', 'Nexon', 'Kia', 'Duster']:
    car = factory.create_instance(carname)
    car.start()
    car.stop()
```

## Classic Factory Pattern

4 Components

- **Abstract Product** : Abstract product class which state what to implement
- **Concrete Product** : Concrete product classes which implements what is abstract
- **Abstract Factory** : Abstract factory which declare create product method
- **Concrete Factory** : Implementes the create product method

1. Update the abstract base class for product (vehicle)

```python
from abc import ABC, abstractmethod


class AbstractAuto(ABC):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
```

2. Implement concrete product classes

```python
from .abstract_auto import AbstractAuto


class Kia(AbstractAuto):
    # init method get's inherited anyway
    # def __init__(self, name):
    #     self.name = name

    def start(self):
        print(f"{self.name} started")

    def stop(self):
        print(f"{self.name} stopped")
```

3. Make a abstract factory class

```python
from abc import ABC, abstractmethod


class AbsFactory(ABC):

    @abstractmethod
    def create_auto(self):
        pass
```

4. Implement abstract factory class and all its methods

```python
from .abstract_factory import AbsFactory
from autos.kia import Kia


class KiaFactory(AbsFactory):

    def create_auto(self):
        self.kia = kia = Kia()
        kia.name = 'Kia SUV'
        return kia
```

5. Now we need a loader which can load specific class when requested

```python
from importlib import import_module
from inspect import getmembers, isabstract, isclass
from .abstract_factory import AbsFactory


def isconcrete(obj):
    return isclass(obj) and not isabstract(obj)


def load_factory(factory_name):
    try:
        factory_module = import_module('.' + factory_name, 'factories')
    except ImportError:
        factory_module = import_module('.null_factory', 'factories')

    classes = getmembers(factory_module, isconcrete)

    for name, _class in classes:
        if issubclass(_class, AbsFactory):
            return _class()
```

6. Client side

```python
from factories import loader

for factory_name in [
        "kia_factory",
        "nano_factory",
        "nexon_factory",
        "null_factory"
]:

    factory = loader.load_factory(factory_name)
    car = factory.create_auto()

    car.start()
    car.stop()
```

## Summary

- Factory method encapsulate instantiation. We no longer need to access classes to instantiate objects instead we call a factory method to do it.
- Support dependency inversion principle. As all concrete product or concrete factories we produced are dependent on abstraction and are not tightly couples with any parent class.
- Client are no longer dependent on implementaton. They don't need to know name of class methods it include as every class is derived form a abstract product and abstract they have some method which are same for all use cases. Also client can access classes via its factory.
- Simple Factory Pattern: Here we have only one factory and we use it to get instance of class we need. Just one factory with several classes.
- Classical Factory Pattern: Here we have several factories one for each class. First we get an instance of factory and then use it to get instance we need.
