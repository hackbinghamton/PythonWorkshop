# Advanced Python Tutorial (Inheritance)
# Author: Melanie Chen
# Based on material from https://docs.python.org/3/tutorial/classes.html

line = "________________________________________________________"

# When possible, we want to avoid rewriting the same code over and over again. Consider the following example:

class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

    def make_noise(self):
        print("Woof")

class Cat:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

    def make_noise(self):
        print("Meow")

# The code is not maintainable - every time we want to add a new behavior for an animal, we must update both the Dog and Cat class. The code is more prone to errors (more typing!) and does not obey the DRY principle.

# Instead, let's create a BASE CLASS that both Dog and Cat classes can inherit from. These will now be called DERIVED CLASSES.

class Animal:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

# For the derived classes, we must indicate in parentheses which base class it inherits from. This base class MUST be in scope.
# If we want to refer to a base class in another module, we can use Module.BaseClassName in parentheses instead.

class Dog(Animal):
    def make_noise(self):
        print("Woof")

class Cat(Animal):
    def make_noise(self):
        print("Meow")

# All the same rules discussed before apply to the instantiation of derived classes. When the class object (Dog or Cat, in this exmaple) is constructed, the base class is remembered. Then when we reference a data attribute or function, we first search the derived class and then the base class.

d = Dog("Fido")
c = Cat("Archer")

print(d.make_noise)
print(c.make_noise)

a = Animal("Arthur")
try:
    print(a.make_noise())
except AttributeError as e:
    print(e)

print(line)

# Inside the derived class, we can also OVERRIDE behaviors from the base class.
class Vehicle:
    def __init__(self, color):
        self.color = color
        self.speed = 0

    def drive_fast(self):
        self.speed = 55

class Car(Vehicle):
    def drive_fast(self):
        self.speed = 65

class Racecar(Vehicle):
    def drive_fast(self):
        self.speed = 105

v = Vehicle("red")
c = Car("blue")
r = Racecar("green")

print(v.speed)
print(c.speed)
print(r.speed)

v.drive_fast()
c.drive_fast()
r.drive_fast()

print(line)

print(v.speed)
print(c.speed)
print(r.speed)

# Why does the constructor Car() take one argument? Don't we need to define an __init__() function for every class?
# The Car class inherits from its base class Vehicle. When we first create an instance object, the scope of the Car class is searched to resolve __init__(). When it is not found, we move to the Vehicle class, where it is found and used.

# Let's say we want to add some functionality to the __init__() method for the Car. How can we preserve the base class functionality wihtout completely overriding it?
# We do so by using the syntax BaseClassName.method(self, args).
class Vehicle:
    def __init__(self, color):
        self.color = color
        self.speed = 0

    def drive_fast(self):
        self.speed = 55

class Car(Vehicle):
    def __init__(self, color):
        Vehicle.__init__(self, color)
        self.fill_fuel()

    def drive_fast(self):
        if fuel > 5:
            self.speed = 65

    def fill_fuel(self):
        self.fuel = 15

class Racecar(Vehicle):
    def drive_fast(self):
        self.speed = 105

c = Car("blue")
print(c.fuel)
print(c.color)

# A derived class can inherit from multiple base classes. Consider the example below:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getAge(self):
        return self.age

class Student:
    def __init__(self, studentId):
        self.id = studentId
    def getStudentId(self):
        return self.id

class Resident:
    def __init__(self, name, age, studentId):
        Person.__init__(self, name, age)
        Student.__init__(self, studentId)

