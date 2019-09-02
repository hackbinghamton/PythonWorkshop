# List Comprehensions

Now that you've learned about Lists, you may find yourself wanting to add multiple items to a list quickly. Now normally you can do this with either of the loops that we've gone over, but there's a simpler, more concise way as well called List Comprehensions.

List Comprehensions are an easy way to create a list with lots of values in it in one single line of code. Let's say you want to add the numbers 0 through 10 to a list. Instead of doing this with a loop like the following code...

```python
my_list = []
for i in range(10):
  my_list.append(i)
```

...we can instead use comprehensions to make our code more streamlined:

```python
my_list = [i for i in range(10)]
```

This will automatically loop 10 times and add every element "i" just like the three lines of code above would.
