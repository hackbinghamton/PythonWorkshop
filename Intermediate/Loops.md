# Loops

One of the most important parts of programming is being able to repeat something over and over again without repeating dozens or even hundreds of lines of code. That's where loops come in.

There are two types of loops used in most of programming: **For** and **While**

## For Loops

For loops are used when you know exactly how many times you want your loop to run.

For example, if you want to print out the string Hello 10 times, we would use this:

```python
for i in range(10):
  print("Hello")
```

There are two important things to note here:

1. **i** is our iterating variable. That's a fancy way of saying that i is a variable that changes after every loop. It's important to remember that i does **not** have to be i, it can be named anything (as long as it's not a key word in Python).

2. **range(10)** tells our loop how many times to run. Changing the number in the () changes how many times it will run.

Now that we know about these two parts of for loops, let's try to print the numbers 0 through 20:

```python
for x in range(21):
  print(x)
```

Here we changed three things:

1. Our iterating variable is called **x** now.

2. We're printing out **x** now instead of "Hello". What this means is that x is going to start out at the first value in our range, 0, and at the end of every loop it will increase by 1.

3. Our range is 21 because we want to print all of the numbers up to 20. Since our loop starts at 0, range(20) would only take us to the number 19. So we have to loop 21 times to get numbers 0 through 20.

## While Loops

While loops are used when we don't know how many times our loop needs to run.

Let's say you want to keep asking a user for input until they enter "q" to exit:

```python
x = ""
while(x != "q"):
  x = input("Please input something (input q to quit)")
```

While loops rely on one single boolean expression, which is an equation that will evaluate to either True or False. As long as that expression evaluates to True, the loop will continue. Once it evaluates to False, the loop ends.

In this case, our boolean expression is `x != "q"`. If the user's input, which is stored in our variable x, is not q then the expression will be True. If it is q, the expression will be False and the loop will stop.

Each time the loop iterates, the user inputs something and it is stored in x. The loop then checks if their input is q and either loops again or stops.

The reason we use a while loop in this situation is that we don't know when the user is going to input q. They could input q before the loop even starts, or they could never input q at all.

The most important part of using a while loop is making sure that your boolean expression will at some point be False. If it is always True and never changes, then your loop will be infinite (a very bad thing). An example of an infinite loop would be:

```python
  while(5 = 5):
    print("Hello")
```

Since 5 = 5 will always be true, the boolean expression is never false and the loop never ends.
