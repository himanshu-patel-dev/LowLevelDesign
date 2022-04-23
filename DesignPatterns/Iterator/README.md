# Iterator Pattern

Iterator is a behavioral design pattern that lets you traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.).

## Python Iterators
Iterator in Python is simply an object that can be iterated upon. An object which will return data, one element at a time.
Technically speaking, a Python iterator object must implement two special methods, `__iter__()` and `__next__()`, collectively called the iterator protocol.

An object is called **iterable** if we can get an **iterator** from it. Most built-in containers in Python like: list, tuple, string etc. are iterables.
The `iter()` function (which in turn calls the `__iter__()` method) returns an iterator from them.

### Iterating Through an Iterator
We use the `next()` function to manually iterate through all the items of an iterator. When we reach the end and there is no more data to be returned, it will raise the `StopIteration` Exception. Following is an example.

```python
# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

# iterate through it using next()

# Output: 4
print(next(my_iter))

# Output: 7
print(next(my_iter))

# next(obj) is same as obj.__next__()

# Output: 0
print(my_iter.__next__())

# Output: 3
print(my_iter.__next__())

# This will raise error, no items left
next(my_iter)
```
```bash
4
7
0
3
Traceback (most recent call last):
  File "<string>", line 24, in <module>
    next(my_iter)
StopIteration
```

Implementing a `for` loop as `while` loop.

```python
for element in iterable:
    # do something with element

# create an iterator object from that iterable
iter_obj = iter(iterable)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break
```

### Building Custom Iterators
Building an iterator from scratch is easy in Python. We just have to implement the `__iter__()` and the `__next__()` methods.

The `__iter__()` method returns the iterator object itself. If required, some initialization can be performed.

The `__next__()` method must return the next item in the sequence. On reaching the end, and in subsequent calls, it must raise StopIteration.

```python
class PowerOfTwo:
    """Class to implement an iterator of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# create an object
numbers = PowerOfTwo(3)

# create an iterable from the object
iterator = iter(numbers)

# Using next to get to the next iterator element
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
```
```bash
1
2
4
8
Traceback (most recent call last):
  File "/home/bsoyuj/Desktop/Untitled-1.py", line 32, in <module>
    print(next(i))
  File "<string>", line 18, in __next__
    raise StopIteration
StopIteration
```

## Problem
Collections are one of the most used data types in programming. `Nonetheless`, a collection is just a container for a group of objects.

But how do you sequentially traverse elements of a complex data structure, such as a tree? For example, one day you might be just fine with depth-first traversal of a tree. Yet the next day you might require breadth-first traversal. And the next week, you might need something else, like random access to the tree elements.

Adding more and more traversal algorithms to the collection gradually blurs its primary responsibility, which is efficient data storage. Additionally, some algorithms might be tailored for a specific application, so including them into a generic collection class would be weird.

## Solution
The main idea of the Iterator pattern is to extract the traversal behavior of a collection into a separate object called an **iterator**.

In addition to implementing the algorithm itself, an iterator object encapsulates all of the traversal details, such as the current position and how many elements are left till the end. Because of this, several iterators can go through the same collection at the same time, independently of each other.

Usually, iterators provide one primary method for fetching elements of the collection. The client can keep running this method until it doesn’t return anything, which means that the iterator has traversed all of the elements.

## Applicability
- Use the Iterator pattern when your collection has a complex data structure under the hood, but you want to hide its complexity from clients (either for convenience or security reasons).
- Use the pattern to reduce duplication of the traversal code across your app.
- Use the Iterator when you want your code to be able to traverse different data structures or when types of these structures are unknown beforehand.

## How to Implement
- Declare the iterator interface. At the very least, it must have a method for fetching the next element from a collection. But for the sake of convenience you can add a couple of other methods, such as fetching the previous element, tracking the current position, and checking the end of the iteration.
- Declare the collection interface and describe a method for fetching iterators. The return type should be equal to that of the iterator interface. You may declare similar methods if you plan to have several distinct groups of iterators.
- Implement concrete iterator classes for the collections that you want to be traversable with iterators. An iterator object must be linked with a single collection instance. Usually, this link is established via the iterator’s constructor.
- Implement the collection interface in your collection classes. The main idea is to provide the client with a shortcut for creating iterators, tailored for a particular collection class. The collection object must pass itself to the iterator’s constructor to establish a link between them.
- Go over the client code to replace all of the collection traversal code with the use of iterators. The client fetches a new iterator object each time it needs to iterate over the collection elements.

## Pros
- Single Responsibility Principle. You can clean up the client code and the collections by extracting bulky traversal algorithms into separate classes.
- Open/Closed Principle. You can implement new types of collections and iterators and pass them to existing code without breaking anything.
- You can iterate over the same collection in parallel because each iterator object contains its own iteration state.
- For the same reason, you can delay an iteration and continue it when needed.
## Cons
- Applying the pattern can be an overkill if your app only works with simple collections.
- Using an iterator may be less efficient than going through elements of some specialized collections directly.

## Implementation
```python
# iterator.py
from collections.abc import Iterator


"""
To create an iterator in Python, there are two abstract classes from the 
built-in `collections` module - Iterable and Iterator. We need to implement the
`__iter__()` method in the iterated object (collection), and the `__next__ ()`
method in the iterator.
"""
# when the collection object is called with iter() method then it return 
# Iterator object, thus to make AlphabeticalOrderIterator as Iterator we
# Inherited from Iterator 
class AlphabeticalOrderIterator(Iterator):
	"""
	Concrete Iterators implement various traversal algorithms. These classes
	store the current traversal position at all times.
	"""

	"""
	`_position` attribute stores the current traversal position. An iterator may
	have a lot of other fields for storing iteration state, especially when it
	is supposed to work with a particular kind of collection.
	"""
	_position: int = None

	"""
	This attribute indicates the traversal direction.
	"""
	_reverse: bool = False

	def __init__(self, collection, reverse: bool = False) -> None:
		self._collections = collection
		self._reverse = reverse
		self._position = -1 if reverse else 0		# deciding whether to start from front or back

	def __next__(self):
		"""
		The __next__() method must return the next item in the sequence. On
		reaching the end, and in subsequent calls, it must raise StopIteration.
		"""
		try:
			value = self._collections[self._position]		# fetch data at current index
			self._position += -1 if self._reverse else 1	# inc index if not reverse traversal else dec
		except IndexError:
			raise StopIteration()

		return value

# collection.py
from collections.abc import Iterable
from typing import Any, List
from iterator import AlphabeticalOrderIterator


class WordsCollection(Iterable):
	"""
	Concrete Collections provide one or several methods for retrieving fresh
	iterator instances, compatible with the collection class.
	"""

	def __init__(self, collections: List[Any] = []) -> None:
		self._collection = collections

	def __iter__(self) -> AlphabeticalOrderIterator:
		"""
		The __iter__() method returns the iterator object itself, by default we
		return the iterator in ascending order.
		"""
		return AlphabeticalOrderIterator(self._collection)

	def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
		return AlphabeticalOrderIterator(self._collection, True)

	def add_item(self, item: Any):
		self._collection.append(item)

# main.py
from collection import WordsCollection


if __name__ == "__main__":
	# The client code may or may not know about the Concrete 
	# Iterator or Collection classes, depending on the level 
	# of indirection you want to keep in your program.
	collection = WordsCollection()
	collection.add_item("First")
	collection.add_item("Second")
	collection.add_item("Third")

	print("Straight traversal:")
	# join take an iterator from collection and iterate over 
	# it to get rest of the elements
	print("\n".join(collection))	
	print("")

	print("Reverse traversal:")
	print("\n".join(collection.get_reverse_iterator()), end="")
```
```bash
Straight traversal:
First
Second
Third

Reverse traversal:
Third
Second
First
```
