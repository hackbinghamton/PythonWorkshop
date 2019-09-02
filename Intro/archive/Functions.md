# Functions
Python uses functions to repurpose code.
The language has many default functions like print, but you can also write your own.
To write your own function start with def and the name of your function followed by ():
then, indented, write what you want your function to do.
for example:

```
def isTwentySixTooManyCats():
  print("probably")
```

To use our function we just need to write it's name followed by parenthesis.

```
isTwentySixTooManyCats()
```

This should print probably.
Alternatively if we write this function with a return statement we can set probably to a variable instead.

```
def isTwentySevenTooManyCats():
  return "yes"
```

Now we can set a new variable to equal the result of the function.

```
truth = isTwentySixTooManyCats()
```
### Print truth to see if it equals yes (it better or I messed up somehow...)

This doesn't seem very useful, but that's because I haven't told you the most important part yet!
Your functions can import information--you put how many variables you want in the parenthesis when you write the function

```
def doIHaveTooManyCats(numCats):
  if numCats <= 15:
    return "no"
  else:
    return "yes"
```

Then when you call the function you put a variable or data in the parenthesis

```print(doIHaveTooManyCats(3))
print(doIHaveTooManyCats(65))

myCats = 437

print(doIHaveTooManyCats(myCats))
```

Your functions can use multiple variables

```
def doYouThinkIHaveTooManyCats(numCats, yourLimit):
  if numCats <= yourLimit:
    return "no, less than "+yourLimit+" is fine."
  else:
    return "yes"

print(doYouThinkIHaveTooManyCats(myCats, 5))
```

### Write your own function that takes a name and returns a greeting along with that name
---
#### <div style="text-align: right"> Next File (Recommended): Boolean Logic </div>
