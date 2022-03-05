## SOLID Principle

`Solid Principle` of Object Oriented Design

### `S` - Single Responsibility

- Class must have a single responsiblity.
- If a class has more than one responsibility, it becomes coupled. A change to one responsibility results to modification of the other responsibility.

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def save(self, animal: Animal):
        pass
```

Above class violetes SRP. we can draw out two responsibilities: animal database management and animal properties management. Lets decouple both the responsiblities of class.

```python
class Animal:
    def __init__(self, name: str):
            self.name = name
    
    def get_name(self):
        pass


class AnimalDB:
    def get_animal(self) -> Animal:
        pass

    def save(self, animal: Animal):
        pass
```  

### `O` - Open Closed

- Software entities(Classes, modules, functions) must be open for modification/extension by inheritance
- Software entities(Classes, modules, functions) must be closed for modification

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

animals = [
    Animal('lion'),
    Animal('mouse')
]

def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')

        elif animal.name == 'mouse':
            print('squeak')

animal_sound(animals)
```

The function `animal_sound` does not conform to the open-closed principle because it cannot be closed against new kinds of animals.
If we add a new animal, `Snake`, We have to modify the `animal_sound` function.

```python
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return 'roar'


class Mouse(Animal):
    def make_sound(self):
        return 'squeak'


class Snake(Animal):
    def make_sound(self):
        return 'hiss'

animals = [
    Lion('lion'),
    Mouse('mouse')
]

def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())

animal_sound(animals)
```

### `L` - Liskov Substitution

- Subclass must be able to subtitute their parent class in programs without breaking anything
- If the code finds itself checking the type of class then, it must have violated this principle.

```python
def animal_leg_count(animals: list):
    for animal in animals:
        if isinstance(animal, Lion):
            print(lion_leg_count(animal))
        elif isinstance(animal, Mouse):
            print(mouse_leg_count(animal))
        elif isinstance(animal, Snake):
            print(snake_leg_count(animal))

animal_leg_count(animals)
```

- If the super-class (Animal) has a method that accepts a super-class type (Animal) parameter. Then its sub-class(Mouse) should accept as argument a super-class type (Animal type) or sub-class type(Mouse type).
- If the super-class returns a super-class type (Animal). Then its sub-class should return a super-class type (Animal type) or sub-class type(Mouse).

```python
def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.leg_count())
        
animal_leg_count(animals)
```

- The `animal_leg_count` function cares less the type of Animal passed, it just calls the `leg_count` method. All it knows is that the parameter must be of an Animal type, either the Animal class or its sub-class.

```python
class Animal:
    def leg_count(self):
        pass

class Lion(Animal):
    def leg_count(self):
        return 4
```

The `animal_leg_count` doesn’t need to know the type of Animal to return its leg count, it just calls the `leg_count` method of the Animal type because by contract a sub-class of Animal class must implement the `leg_count` function.

### `I` - Interface Segregation

- Many specific interface are better than do it all interface
- Make fine grained interfaces that are client specific Clients should not be forced to depend upon interfaces that they do not use.

```python
# Parant Class
class IShape:
    def draw_square(self):
        raise NotImplementedError
    
    def draw_rectangle(self):
        raise NotImplementedError
    
    def draw_circle(self):
        raise NotImplementedError

# Sub Classes
class Circle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass
    
    def draw_circle(self):
        pass

class Square(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass
    
    def draw_circle(self):
        pass
```

- Class `Rectangle` implements methods (`draw_circle` and `draw_square`) it has no use of. If we add another method to the IShape interface, like `draw_triangle()`
- Previous classes must implement all new method or error will be thrown.

```python
class IShape:
    def draw_square(self):
        raise NotImplementedError
    
    def draw_rectangle(self):
        raise NotImplementedError
    
    def draw_circle(self):
        raise NotImplementedError
    
    def draw_triangle(self):
        raise NotImplementedError
```

- To make our IShape interface conform to the ISP principle, we segregate the actions to different interfaces. Classes (Circle, Rectangle, Square, Triangle, etc) can just inherit from the IShape interface and implement their own draw behavior.

```python
class IShape:
    def draw(self):
        raise NotImplementedError

class Circle(IShape):
    def draw(self):
        pass

class Square(IShape):
    def draw(self):
        pass

class Rectangle(IShape):
    def draw(self):
        pass
```

- We can then use the I -interfaces to create Shape specifics like Semi Circle, Right-Angled Triangle, Equilateral Triangle, Blunt-Edged Rectangle, etc.

### `D` - Dependency Inversion

- We should program towards abstraction and not implementation
- Dependency should be on abstractions not concretions
- **A**. High-level modules should not depend upon low-level modules. Both should depend upon abstractions.
- **B**. Abstractions should not depend on details. Details should depend upon abstractions.

```python
# Without Dependency Inversion

class LightBulb:
    def turn_on(self):
        print('LightBulb: turned on')

    def turn_off(self):
        print('LightBulb: turned off')

class ElectricPowerSwitch:
    def __init__(self, l: LightBulb):
        self.lightbulb = l
        self.on = False

    def press(self):
        if self.on:
            self.lightbulb.turn_off()
            self.on = False
        else:
            self.lightbulb.turn_on()
            self.on = True

l = LightBulb()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()
```

Here `ElectricPowerSwitch` is dependent on `LightBulb` class and its methods. Here if we want to declare `Fan` class then we need to specify input parameter `l` to be of Fan type which is not possible until we make a new class similar to `ElectricPowerSwitch`. Here we can only . To solve this problem we use **Dependency Inversion** which is decoupling the High Level class from Low Level class.

We can have **Abstract Base Class** in python and type hints to bring this abstraction.

```python
from abc import ABC, abstractmethod, abstractproperty

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass

    @abstractproperty
    def device(self):
        pass

# we can't instantiate an abstract class neither 
# any other class which inherit abstract class and 
# do not implement even one of its abstractmethod 

# s = Switchable()
```

See how we efficitevly decouple the `LightBulb` and `ElectricPowerSwitch` using `Switchable` class.

```python
class LightBulb(Switchable):
    def turn_on(self):
        print('LightBulb: turned on')

    def turn_off(self):
        print('LightBulb: turned off')

    @property
    def device(self):
        return "Bulb"


class ElectricPowerSwitch:
    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True

l = LightBulb()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()

# LightBulb: turned on
# LightBulb: turned off
# Bulb
```

Now we can pass not only `LightBulb` but any other class implemented `Switchable` class like `Fan`.

```python
class Fan(Switchable):
    def turn_on(self):
        print('Fan: turn on')

    def turn_off(self):
        print('Fan: turn off')

    @property
    def device(self):
        return "Fan"


class ElectricPowerSwitch:
    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True

f = Fan()
switch = ElectricPowerSwitch(f)
switch.press()
switch.press()

# Fan: turn on
# Fan: turn off
# Fan
```
