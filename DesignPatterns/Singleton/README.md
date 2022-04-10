# Singleton Pattern

**Classification**: Creational

This pattern is used for creation of object. Infact Singleton enfore that class must have only one object. This provide global point of access. Also class is reponsible for its one intance. Also provide **lazy** instantiation if object is costly to instantiate or less likely to use.

## Problem
The Singleton pattern solves two problems at the same time, but violating the Single Responsibility Principle:

1. Ensure that a class has just a single instance. Like to control access to some shared resource—for example, a database or a file. 

2. Provide a global access point to that instance. Remember those global variables that you used to store some essential objects? While they’re very handy, they’re also very unsafe since any code can potentially overwrite the contents of those variables and crash the app.

Just like a global variable, the Singleton pattern lets you access some object from anywhere in the program. However, it also protects that instance from being overwritten by other code.

## Solution
All implementations of the Singleton have these two steps in common:

1. Make the default constructor private, to prevent other objects from using the new operator with the Singleton class.

2. Create a static creation method that acts as a constructor. Under the hood, this method calls the private constructor to create an object and saves it in a static field. All following calls to this method return the cached object.

If your code has access to the Singleton class, then it’s able to call the Singleton’s static method. So whenever that method is called, the same object is always returned.

## Applicability
1. Use the Singleton pattern when a class in your program should have just a single instance available to all clients; for example, a single database object shared by different parts of the program.
2. Use the Singleton pattern when you need stricter control over global variables.

## How to Implement
1. Add a private static field to the class for storing the singleton instance. Declare a public static creation method for getting the singleton instance.

2. Implement “lazy initialization” inside the static method. It should create a new object on its first call and put it into the static field. The method should always return that instance on all subsequent calls.

3. Make the constructor of the class private. The static method of the class will still be able to call the constructor, but not the other objects.

4. Go over the client code and replace all direct calls to the singleton’s constructor with calls to its static creation method.

## Pros and Cons

### Pros
- You can be sure that a class has only a single instance.
- You gain a global access point to that instance.
- The singleton object is initialized only when it’s requested for the first time.
### Cons
-  Violates the Single Responsibility Principle. The pattern solves two problems at the time.
- The Singleton pattern can mask bad design, for instance, when the components of the program know too much about each other.
- The pattern requires special treatment in a multithreaded environment so that multiple threads won’t create a singleton object several times.
- It may be difficult to unit test the client code of the Singleton because many test frameworks rely on inheritance when producing mock objects. Since the constructor of the singleton class is private and overriding static methods is impossible in most languages, you will need to think of a creative way to mock the singleton. Or just don’t write the tests. Or don’t use the Singleton pattern.

## Implementation

### `__call__` in Python

The `__call__` method enables Python programmers to write classes where the instances behave like functions and can be called like a function. When the instance is called as a function; if this method is defined, `x(arg1, arg2, ...)` is a shorthand for `x.__call__(arg1, arg2, ...)`. `object()` is shorthand for `object.__call__()`.

```python
class Product:
    def __init__(self):
        print("Instance Created")
  
    # Defining __call__ method
    def __call__(self, a, b):
        print(a * b)
  
# Instance created
ans = Product()
  
# __call__ method will be called
ans(10, 20)

## OUTPUT
# Instance Created
# 200
```

### `__dict__` in python  
A dictionary or other mapping object used to store an object’s (writable) attributes.

```python
>>> class MyClass:
...     class_attribute = "iamclass"
... 
>>> a = MyClass()
>>> a.__dict__
{} 
>>> a.class_attribute
'iamclass'
>>> a.obj_attribute = "iamobj"
>>> a.obj_attribute
'iamobj'
>>> a.__dict__
{'obj_attribute': 'iamobj'}
```

## Simple Example

```python
class Singleton:
	ans = None

	@staticmethod
	def instance():
		if '_instance' not in Singleton.__dict__:
			Singleton._instance = Singleton()
		return Singleton._instance

s1 = Singleton.instance()
s2 = Singleton.instance()
s1.ans = 10

print(s1 is s2)
print(s1.ans == s2.ans)
print(id(s1) == id(s2))

# True
# True
# True
```

While using `@staticmethod` we dont pass `self` parameter to method.

## Classic Example : Logger

A more classic example is of Logger which need only one instance of class for execution and loggin all the required activities.

```python
import datetime

class Logger:
    log_file = None

    @staticmethod
    def instance():
        if '_instance' not in Logger.__dict__:
            Logger._instance = Logger()
        return Logger._instance

    def open_log(self, path):
        self.log_file = open(path, mode='w')
        self.log_file.writelines('\n')

    def write_log(self, log_record):
        now = str(datetime.datetime.now().strftime("%m-%d-%Y, %H:%M:%S"))
        record = f"{now}: {log_record}"
        self.log_file.writelines(record)
    
    def close_log(self):
        self.log_file.close()


logger = Logger.instance()  # notice not Logger() but Logger.instance()
logger.open_log('MyLog.log')
logger.write_log('Logger with classic Singleton pattern')
logger.close_log()

with open('MyLog.log', 'r') as log:
    for line in log:
        print(line)
```

Singleton is called **antipattern** because some of the cons.

- **Violates Single Responsiblity Priciple**: Same logger class is making a file connection and maintaining it.

- **Non-Standard class access**: To get instance we must know the class is singleton and then use `_instance` method to get already instantiated object.

- **Testing**: They make unit testing very hard. They introduce global state to the application. The problem is that you cannot completely isolate classes dependent on singletons. Difficult to make mockups.

## 1. Base Class Example : Fix Single Responsiblity Problem

Building a base class for all singleton.

Whenever a class is instantiated `__new__` and `__init__` methods are called. `__new__` method will be called when an object is created and `__init__` method will be called to initialize the object.

`__new__` is the first step of instance creation. It's called first and is responsible for returning a new instance of your class. In contrast, `__init__` doesn't return anything; it's only responsible for initializing the instance after it's been created.

```python
class MyClass:
    def __new__(cls):
        print("Making new object")
        return super(MyClass, cls).__new__(cls)

    def __init__(self):
        print("Initializing new object")

obj = MyClass()
print('-- obj created --')

# Making new object
# Initializing new object
# -- obj created --
```

### Logger with Base Singleton class

```python
# singleton_baseclass.py

import datetime

class Singleton:
    _instances = {}     # dict([cls, instance])

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]

# from singleton_baseclass import Singleton

class Logger(Singleton):
    log_file = None

    # need for open file method is removed
    def __init__(self, path):
        if not self.log_file:
            self.log_file = open(path, 'w')
    
    def write_log(self, log_record):
        now = datetime.datetime.now().strftime("%m-%d-%Y, %H:%M:%S")
        record = f"{now}: {log_record}"
        self.log_file.writelines(record + "\n")

    def close_log(self):
        if self.log_file:
            self.log_file.close()
            self.log_file = None

# need for Logger.instance() is removed
logger1 = Logger('MyLog2.log')
logger1.write_log('First Line of log')
logger2 = Logger('SameLogFile.log')
logger2.write_log('Second Line of log')
logger1.close_log()
logger2.close_log()


with open('MyLog2.log', 'r') as log:
    for line in log:
        print(line)
```

In `MyLog2.log`. Notice `SameLogFile.log` is not even created as long as first object of Logger is present.

```text
06-01-2021, 10:20:20: First Line of log
06-01-2021, 10:20:20: Second Line of log
```

## 2. Meta Class Example : Class's class

Each class is an instance of its metaclass. A class can control it's instances. Hence we use a meta class to control all the instance of its subclass they can create a new instance only it there do not exists one already.

```python
import datetime

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

# from singleton_metaclass import Singleton

class Logger(metaclass=Singleton):
    log_file = None

    # need for open file method is removed
    def __init__(self, path):
        if not self.log_file:
            self.log_file = open(path, 'w')

    def write_log(self, log_record):
        now = datetime.datetime.now().strftime("%m-%d-%Y, %H:%M:%S")
        record = f"{now}: {log_record}"
        self.log_file.writelines(record)

    def close_log(self):
        if self.log_file:
            self.log_file.close()
            self.log_file = None


logger1 = Logger('MyLog3.log')
logger1.write_log('First Line of log')
logger2 = Logger('SameLogFile.log')
logger2.write_log('Second Line of log')
logger1.close_log()
logger2.close_log()


with open('MyLog2.log', 'r') as log:
    for line in log:
        print(line)
```

## 3. Monostate Example: Maintain state of all instances

It maintains a dictionary maintaining a single state for all instances.

```python
import datetime

# it maintains a dictionary maintaining a single state for all instances
class MonoState(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        # create a new instance
        self = super().__new__(cls)	
        # new instance have same properties as prev instance
        self.__dict__ = cls._state
        # return new instance
        return self

# from singleton_monostate import MonoState

class Logger(MonoState):
    log_file = None

    # need for open file method is removed
    def __init__(self, path):
        if not self.log_file:
            self.log_file = open(path, 'w')

    def write_log(self, log_record):
        now = datetime.datetime.now().strftime("%m-%d-%Y, %H:%M:%S")
        record = f"{now}: {log_record}"
        self.log_file.writelines(record)

    def close_log(self):
        if self.log_file:
            self.log_file.close()
            self.log_file = None


logger1 = Logger('MyLog4.log')
logger1.write_log('First Line of log')
logger2 = Logger('MyLog4_2.log')
logger2.write_log('Second Line of log')
logger1.close_log()
logger2.close_log()


with open('MyLog4.log', 'r') as log:
    for line in log:
        print(line)
```

To better understand MonoState

```python
>>> c = MonoState()
>>> c.__dict__
{}
>>> c.art1 = "Hello"
>>> c.__dict__
{'art1': 'Hello'} 
>>> d = MonoState()
>>> d.__dict__
{'art1': 'Hello'}
```

## 4. Thread Safe: Singleton

It’s pretty easy to implement a sloppy Singleton. You just need to hide the constructor and implement a static creation method.

The same class behaves incorrectly in a multithreaded environment. Multiple threads can call the creation method simultaneously and get several instances of Singleton class. To fix the problem, you have to **synchronize threads during the first creation of the Singleton object**.

### How to lock Critical Sections

```python
import threading
  
class CounterShare:
    '''
    multiple threads can share.
    '''
    def __init__(self, initial_key = 0):
        self._key = initial_key
        self._key_lock = threading.Lock()
          
    def incr(self, delta = 1):
        with self._key_lock:
            # Increasing the counter with lock
            self._key += delta
          
    def decr(self, delta = 1):
        with self._key_lock:
            # Decreasing the counter with lock
            self._key -= delta
```

Using a `with` statement along with the `lock` ensures the mutual exclusion. By exclusion, it is meant that at a time only one thread (under with statement) is allowed to execute the block of a statement. Also the `with` statement is much less prone to error.


```python
from multiprocessing.sharedctypes import Value
from threading import Lock, Thread
from tokenize import single_quoted

class SingletonMeta(type):
	"""
	This is a thread-safe implementation of Singleton.
	"""
	_instances = {}
	_lock = Lock()
	"""
	We now have a lock object that will be used to synchronize threads during
	first access to the Singleton.
	"""

	def __call__(cls, *args, **kwds):
		"""
		Possible changes to the value of the `__init__` argument do not affect
		the returned instance.

		Now, imagine that the program has just been launched. Since there's no
		Singleton instance yet, multiple threads can simultaneously pass the
		previous conditional and reach this point almost at the same time. The
		first of them will acquire lock and will proceed further, while the
		rest will wait here.        
		"""
		with cls._lock:		# acquiring lock at start of context manager and release on exit
			if cls not in cls._instances:
				cls._instances[cls] = super().__call__(*args, **kwds)
			return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
	value:str = None
	"""
	We'll use this property to prove that our Singleton really works.
	"""

	def __init__(self, value: str) -> None:
		self.value = value

	def business_logic(self):
		"""
		Finally, any singleton should define some business logic, which can be
		executed on its instance.
		"""

def test_singleton(value):
	"""
	This function is for thread
	"""
	singleton = Singleton(value)
	print(singleton.value)

if __name__ == "__main__":
	# The client code.

	print("If you see the same value, then singleton was reused (yay!)\n"
		  "If you see different values, "
		  "then 2 singletons were created (booo!!)\n\n"
		  "RESULT:\n")

	process1 = Thread(target=test_singleton, args=("FOO",))	# this , matters
	process2 = Thread(target=test_singleton, args=("BAR",))
	process1.start()
	process2.start()

# If you see the same value, then singleton was reused (yay!)
# If you see different values, then 2 singletons were created (booo!!)

# RESULT:

# FOO
# FOO
```
