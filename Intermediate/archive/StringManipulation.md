# String Manipulation

Now that we know about Lists, we can revisit strings and take a closer look at ways to use them.

Strings are really just a list of characters. For instance, the string "Hello World" is a list of 11 characters. Just like any other list, we can access elements of it by using their index. The following code should print the character at index 0 in "Hello World", which is "H":

```python
my_string = "Hello World"
print(my_string[0])
```
### Concatenation

Strings can be added together just like lists. For example, if we take the string "Hello" and add it to the string "World":

```python
my_string = "Hello" + "World"
print(my_string)
```

Notice that this doesn't add a space in between the two strings. You must include this yourself either at the end of the first string or at the beginning of the second string.


Strings also have a lot of built in functions in Python that make using them much easier:

### Count

count() will return the number of occurrences of a given string within your string. Let's say you need to count the number of times that "g" shows up in a string that the user inputs. The syntax for this is `string_name.count("g")`.

### Slicing

Slicing lets you take a small chunk of characters out of a string and store it in a new string. Syntactically, slicing is similar to indexing. The basic form is **[start : end]** where start and end are indexes in the string. For example, `my_string[0:3]` will give you a string of the first three characters in my_string. The following code should print "Doct":

```python
my_string = "Doctor"
new_string = my_string[0:4]
print(new_string)
```

Notice that the string that is returned will include the character at the start index, but will only include up to the character at one less than the end index. Not passing in a value for start will automatically make it 0, and not passing in a value for end will automatically make it the last index in the string + 1.

The indexes can also be negative, so `my_string[-3:]` will return the last three characters of the string and `my_string[:-3]` will give you all but the last three characters of the string.

### Split

split() allows you to turn a string into a list of strings. The original string will be split apart at every occurrence of the string that is passed into split(). For example, the following code will print ["My", "dog", "is", "great"]

```python
my_string = "My dog is great"
split_string = my_string.split(" ")
print(split_string)
```
