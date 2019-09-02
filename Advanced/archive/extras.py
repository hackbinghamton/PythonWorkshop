# Advanced Python Tutorial (Extras)
# Author: Melanie Chen
# Based on material from https://docs.python.org/3/tutorial/classes.html

line = "________________________________________________________"
# Classes are created at runtime and can be modified after creation
# Python is an object-oriented PL:
    # Allows multiple base classes
    # Derived class can override any method of its base class(es)
    # Derived class method can call the method of a base class with the same name

# To override behavior where a local variable is distinct from the variable in the enclosing scope of the same name, we can use the nonlocal statement.

def my_enclosing():
    def my_fun():
        # Local x
        nonlocal x
        x = 4
        print(x)
    
    x = 5
    print(x)
    my_fun()
    print(x)

my_enclosing()

print(line)

# The global statement indicates that particular variables live in the global scope and should be bound there.

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
