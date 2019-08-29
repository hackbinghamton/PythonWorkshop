# Collections

Python has a few different ways that you can create collections. Collections make it easy to store large amounts of values into just one variable. The two most common types are **Lists** and **Dictionaries**.

## Lists

Lists are Python's equivalent of Arrays. They store multiple values of the same type, and those values can be accessed by their index in the list. Lists are very easy to instantiate:

```python
mylist = []
```

This will make an empty list with no elements. This doesn't really help us, so let's make a list with a few things in it:

```python
pets = ["Dog", "Cat", "Fish"]
```

Now we have a list of three strings. We can access elements by using `pets[i]`, which will give us the item at index i of the list. Since programming always starts counting at 0, `pets[0]` will give us the first element of the list, which is "Dog". So the following code should print "Dog".

```python
pets = ["Dog", "Cat", "Fish"]
pet_dog = pets[0]
print(pet_dog)
```

You can also change elements of the list using the same syntax. The following code should now print "Bird"

```python
pets = ["Dog", "Cat", "Fish"]
pets[1] = "Bird"
print(pets[1])
```

If you want to add an element to a list without changing one that's currently in it, you can use the append() function. This will add a value to the end of the list:

```python
pets = ["Dog", "Cat", "Fish"]
pets.append("Bird")
```

Removing an element from the list is just as easy:

```python
pets = ["Dog", "Cat", "Fish"]
pets.remove("Fish")
```

## Dictionaries

Sometimes you don't want to access elements of a collection by their index. Instead, you might want to associate keys with every value in your collection. This key-value pair is the idea behind dictionaries.

A dictionary is very similar in syntax to lists, but uses {} instead of []. So making a new Dictionary looks like this:

```python
my_dict = {}
```

And making a dictionary with values in it looks like this:

```python
pets = {"Dog": "Rufus", "Cat": "Ringo", "Fish": "Bubbles"}
```

For every entry, the basic format is **Key: Value**. The keys must always be strings, but the values can be any data type.

Now we have a dictionary of pets with the type of animal as the key and the name of that animal as the value. Instead of using indexes to access values, we can now just use the keys we've made:

```python
pets = {"Dog": "Rufus", "Cat": "Ringo", "Fish": "Bubbles"}
my_dog = pets["Dog"]
```

This will store the value associated with the key "Dog" into the **my_dog** variable, which in this case will be "Rufus". It's important to note that even though we use {} around a dictionary itself, we still use [] to access elements of the dictionary.

Adding elements to the dictionary or changing values associated with keys already in the dictionary is done very similarly:

```python
pets = {"Dog": "Rufus", "Cat": "Ringo", "Fish": "Bubbles"}
pets["Bird"] = "Polly"
```

Now the list will have a fourth element with key "Bird" and value "Polly".

Removing an element from a dictionary is very similar to removing from a list, but the function is called pop() instead of remove(). This will remove both the key and the value from the dictionary. :

```python
pets = {"Dog": "Rufus", "Cat": "Ringo", "Fish": "Bubbles"}
pets.pop("Fish")
```
