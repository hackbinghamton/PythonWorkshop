# Classes

Based on material from https://docs.python.org/3/tutorial/classes.html

First, we'll need some definitions so you can understand the literature about classes and inheritance in any programming language.

## Class
What is a CLASS? Classes are simply a way to bundle data and functionality together. Creating a new class creates a new TYPE of object, allowing new INSTANCES of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Each class instance can also have methods attached to it for modifying state.

Multiple names (in multiple scopes) can be bound to the same object. This is often known as aliasing. Since aliases behave like pointers in some respects, passing objects is cheap. This also means that if a function modifies an object passed as an argument, the caller will see the change. Consider the example below:

```python
class Room:
    def __init__(self, color, windows, doors):
        self.color = color
        self.windows = windows
        self.doors = doors

def paintRoom(room, color):
    room.color = color

my_room = Room("purple", 2, 1)
print(my_room.color)
paintRoom(my_room, "green")
print(my_room.color)
```

Don't worry too much about the specific syntax of the class. You should observe, however, how passing the object my_room into the function paintRoom() changes its color from purple to green and that this change persists outside of the paintRoom() function.

## Namespace

You'll also need to consider the notion of a NAMESPACE. A NAMESPACE is a mapping from names to objects. Examples include: the set of built-in names (like abs()), global names in a module, and local names in a function invocation. There is no relation between names in different namespaces. Consider the following:

```python
import example1
import example2

print(example1.maximize([5,6,2,7]))
print(example2.maximize([5,6,2,7]))
```

The name maximize is used to refer to two different functions (one in the module example1 and the other in module example2 - you can check these files out!), but neither has anything to do with the other.

## Attribute 

The name maximize also goes by another term: ATTRIBUTE. An ATTRIBUTE is any name following a dot. For example, in the expression z.real, real is an attribute of the object z. Attributes can be read-only or writable. Writable attributes can be modified or deleted.

```python
example1.hello = "Hello, World!"
print(example1.hello)
del example1.hello
try:
    print(example1.hello)
except AttributeError as e:
    print(e)
```

## Scope

Finally, the concept of SCOPE is important to understand. A SCOPE is a textual region of a Python program where a namespace is directly accessible. "Directly accessible" means an unqualified reference to the name attempts to find the name in the namespace. For example, example1.maximize is the full qualified name, whereas maximize is the unqualified name. When a program is trying to resolve a name, it searched in the following order: innermost scope (local names) -> scopes of enclosing functions (non-local, but non-global names) -> next-to-last scope (current module's global names) -> outermost scope (built-in names).

In the example below, the x declared within the function my_fun() is local to that function and its scope does not extend outside of my_fun(). It has nothing to do with the x declared within my_enclosing(), thus the statement prints 5 (outer x), then 4 (inner x), then 5 (outer x, after my_fun() returns).

```python
def my_enclosing():
    def my_fun():
        # Local x
        x = 4
        print(x)
    
    x = 5
    print(x)
    my_fun()
    print(x)

my_enclosing()
```

## Defining a class

Before we can use a class, we must know how to define it. The below syntax describes the most basic class definition.

```python
class MyClass:
    # Data and methods go here
```

When a class definition is entered, a new namespace is created and used as the local scope. When a class definition is exited, a CLASS OBJECT is created. We return to the original scope and the class object is now bound to the class name (e.g. MyClass). We can do two things with this class object, attribute references and instantiation.

## Attribute references

Attribute references use the same syntax used for all attribute references in Python.

```python
class SimpleExample:
    '''This is a docstring'''
    my_data = 42

    def get_my_data(self):
        return my_data

print(SimpleExample.my_data)
print(SimpleExample.get_my_data)
```

## Class instantiation

Class instantiation uses function notation. Pretend the class object is a parameterless function that returns a new INSTANCE of the class. In other words, the class object is like the blueprint and the class instance is like the actual house.

```python
my_simple_example = SimpleExample()
```

Let's keep going with the blueprint-house analogy. What if we want all the houses to share some common features? When a class defines the __init__() method, class instantiation automatically invokes __init__().

```python
class House:
    street = "Leroy Avenue"

    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms
        self.levels = 2
```

Every house starts out with two levels, plus the color and number of rooms that a homeowner chooses. These instance variables contain the state.

Say the homeowner later renovates and adds another room.

```python
    def setNumRooms(self, numRooms):
        self.rooms = numRooms
```

This class method modifies the state.

## Getters and setters

It is common for programmers to define getters and setters for their instance variables. This helps encapsulate code (gives programmers access to an object's state without exposing all its internal implementation details).

```python
    def getNumRooms(self):
        return self.rooms

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setLevels(self, levels):
        self.levels = levels

    def getLevels(self):
        return self.levels
```

## Using instance objects

What can we do with instance objects? We can reference their attributes (data attributes and methods)!

First, let's initialize the class instance using the __init__() method (called a constructor in some languages).

```python
my_house = House("gray", 4)
```

Now, let's reference a data attribute.

```python
print(my_house.rooms)
```

Or, let's reference a method.

```python
print(my_house.getColor())
```

What is the difference between House.getColor() and my_house.getColor()? Technically House.getColor() is a function object and my_house.getColor() is a method object. But, an easier way to think about it is that my_house.getColor() is equivalent to MyHouse.getColor(my_house). Basically, "self" refers to that particular instance object.

Let's see an example.
```python
class Dog:
    kind = "canine"

    def __init__(self, name):
        self.name = name

d = Dog("Fido")
e = Dog("Buddy")

print(Dog.kind)
print(Dog.__init__)
print(d.kind)
print(d.name)
print(e.kind)
print(e.name)
```

## Instance vs. Class Variables

In this example, the kind variable is a class variable. Its state is shared by all instances of the Dog class. The name variable is an instance variable. It is tied to one particular instance.

What's wrong with this example?
```python
class Dog:
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
```
The tricks variable is a class variable, which means every instance of Dog shares its state. This is like a static variable in Java. If Fido learns a new trick, Buddy should not also gain this skill! This variable is better suited as an instance variable.

## Miscellaneous
More on self: The first argument of a method is conventionally called self, but there is nothing special about this word. We could use "me" instead, for example. 

We already know how to reference data attributes and methods from outside the class, but what about within it? Simple prefix the call with self.
```python
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

    def add_many_tricks(self, listOfTricks):
        for trick in listOfTricks:
            self.add_trick(trick)
```

